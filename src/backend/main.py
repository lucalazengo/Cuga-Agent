"""
Cuga Agent - Backend API
MVP de uma plataforma SaaS para análise de tendências de conteúdo TikTok e YouTube
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import sqlite3
from datetime import datetime
import os

# Configurações
DATABASE_PATH = "cuga_agent.db"
ANALYSIS_LIMIT_FREE = 5  # Análises gratuitas por mês
ANALYSIS_LIMIT_STARTER = 50

app = FastAPI(title="Cuga Agent API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class AnalysisRequest(BaseModel):
    niche: str = Field(..., description="Nicho de conteúdo para análise")
    platform: str = Field(..., description="Plataforma: 'tiktok' ou 'youtube'")
    limit: int = Field(20, ge=1, le=100, description="Número de vídeos para analisar")

class VideoData(BaseModel):
    title: str
    url: str
    views: int
    likes: Optional[int] = None
    comments: Optional[int] = None
    shares: Optional[int] = None
    author: str
    thumbnail: Optional[str] = None
    created_at: str
    viral_score: float

class AnalysisResult(BaseModel):
    analysis_id: str
    niche: str
    platform: str
    status: str
    total_videos: int
    videos: List[VideoData]
    created_at: str

class ScriptRequest(BaseModel):
    title: str
    video_data: Optional[VideoData] = None

class ScriptResponse(BaseModel):
    script: str
    structure: dict

# Inicializar banco de dados
def init_db():
    """Inicializa o banco de dados SQLite"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            plan TEXT DEFAULT 'free',
            analyses_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Tabela de análises
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id TEXT PRIMARY KEY,
            user_id INTEGER,
            niche TEXT NOT NULL,
            platform TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            total_videos INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    
    # Tabela de vídeos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            analysis_id TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            views INTEGER NOT NULL,
            likes INTEGER,
            comments INTEGER,
            shares INTEGER,
            author TEXT,
            thumbnail TEXT,
            viral_score REAL,
            created_at TEXT,
            FOREIGN KEY(analysis_id) REFERENCES analyses(id)
        )
    """)
    
    conn.commit()
    conn.close()

# Dependências
def get_db():
    """Retorna conexão com o banco de dados"""
    conn = sqlite3.connect(DATABASE_PATH)
    try:
        yield conn
    finally:
        conn.close()

def get_or_create_user(email: str = "demo@example.com"):
    """Obtém ou cria um usuário demo (simplificado para MVP)"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, plan, analyses_count FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    
    if not user:
        cursor.execute(
            "INSERT INTO users (email, plan) VALUES (?, ?)",
            (email, "free")
        )
        conn.commit()
        user_id = cursor.lastrowid
        plan = "free"
        analyses_count = 0
    else:
        user_id, plan, analyses_count = user
    
    conn.close()
    return {"id": user_id, "plan": plan, "analyses_count": analyses_count}

# Rotas
@app.on_event("startup")
async def startup_event():
    """Inicializa o banco de dados ao iniciar a aplicação"""
    init_db()
    print("✅ Database initialized")

@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "Cuga Agent API - MVP",
        "version": "1.0.0",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Verifica saúde da API"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/api/analyze", response_model=AnalysisResult)
async def analyze_trends(request: AnalysisRequest, email: str = "demo@example.com"):
    """
    Analisa tendências de um nicho específico
    """
    # Verificar limite do usuário
    user = get_or_create_user(email)
    limit = ANALYSIS_LIMIT_FREE if user["plan"] == "free" else ANALYSIS_LIMIT_STARTER
    
    if user["analyses_count"] >= limit:
        raise HTTPException(
            status_code=403,
            detail=f"Limite de análises atingido. Seu plano permite {limit} análises por mês."
        )
    
    # Importar módulos de coleta
    from api_collectors import collect_tiktok_data, collect_youtube_data
    from ranking_algorithm import calculate_viral_score
    
    # Coletar dados
    if request.platform == "tiktok":
        raw_videos = collect_tiktok_data(request.niche, request.limit)
    elif request.platform == "youtube":
        raw_videos = collect_youtube_data(request.niche, request.limit)
    else:
        raise HTTPException(status_code=400, detail="Plataforma inválida. Use 'tiktok' ou 'youtube'")
    
    if not raw_videos:
        raise HTTPException(status_code=404, detail="Nenhum vídeo encontrado para esse nicho")
    
    # Calcular scores de viralidade
    videos_with_scores = []
    for video in raw_videos:
        score = calculate_viral_score(video, request.platform)
        video["viral_score"] = score
        videos_with_scores.append(video)
    
    # Ordenar por score
    videos_with_scores.sort(key=lambda x: x["viral_score"], reverse=True)
    
    # Salvar no banco de dados
    analysis_id = f"analysis_{datetime.now().timestamp()}"
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO analyses (id, user_id, niche, platform, status, total_videos) VALUES (?, ?, ?, ?, ?, ?)",
        (analysis_id, user["id"], request.niche, request.platform, "completed", len(videos_with_scores))
    )
    
    for video in videos_with_scores:
        cursor.execute(
            """INSERT INTO videos (analysis_id, title, url, views, likes, comments, shares, author, thumbnail, viral_score, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                analysis_id,
                video["title"],
                video["url"],
                video["views"],
                video.get("likes"),
                video.get("comments"),
                video.get("shares"),
                video["author"],
                video.get("thumbnail"),
                video["viral_score"],
                video["created_at"]
            )
        )
    
    # Atualizar contador de análises do usuário
    cursor.execute(
        "UPDATE users SET analyses_count = analyses_count + 1 WHERE id = ?",
        (user["id"],)
    )
    
    conn.commit()
    conn.close()
    
    # Preparar resposta
    videos_data = [
        VideoData(
            title=video["title"],
            url=video["url"],
            views=video["views"],
            likes=video.get("likes"),
            comments=video.get("comments"),
            shares=video.get("shares"),
            author=video["author"],
            thumbnail=video.get("thumbnail"),
            created_at=video["created_at"],
            viral_score=video["viral_score"]
        )
        for video in videos_with_scores
    ]
    
    return AnalysisResult(
        analysis_id=analysis_id,
        niche=request.niche,
        platform=request.platform,
        status="completed",
        total_videos=len(videos_data),
        videos=videos_data,
        created_at=datetime.now().isoformat()
    )

@app.post("/api/generate-script", response_model=ScriptResponse)
async def generate_script(request: ScriptRequest, email: str = "demo@example.com"):
    """
    Gera um roteiro simples baseado em um título
    """
    from ai_agent import generate_content_script
    
    try:
        script_data = generate_content_script(request.title)
        return ScriptResponse(
            script=script_data["script"],
            structure=script_data["structure"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar roteiro: {str(e)}")

@app.get("/api/analyses")
async def get_analyses(email: str = "demo@example.com", limit: int = 10):
    """
    Lista análises anteriores do usuário
    """
    user = get_or_create_user(email)
    conn = sqlite3.connect(DATABASE_PATH)
    
    cursor = conn.cursor()
    cursor.execute(
        """SELECT a.id, a.niche, a.platform, a.status, a.total_videos, a.created_at
           FROM analyses a
           WHERE a.user_id = ?
           ORDER BY a.created_at DESC
           LIMIT ?""",
        (user["id"], limit)
    )
    
    analyses = []
    for row in cursor.fetchall():
        analyses.append({
            "analysis_id": row[0],
            "niche": row[1],
            "platform": row[2],
            "status": row[3],
            "total_videos": row[4],
            "created_at": row[5]
        })
    
    conn.close()
    return {"analyses": analyses}

@app.get("/api/analyses/{analysis_id}", response_model=AnalysisResult)
async def get_analysis_detail(analysis_id: str, email: str = "demo@example.com"):
    """
    Obtém detalhes de uma análise específica
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Buscar análise
    cursor.execute("""
        SELECT niche, platform, status, total_videos, created_at
        FROM analyses
        WHERE id = ?
    """, (analysis_id,))
    
    analysis_row = cursor.fetchone()
    if not analysis_row:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    
    niche, platform, status, total_videos, created_at = analysis_row
    
    # Buscar vídeos
    cursor.execute("""
        SELECT title, url, views, likes, comments, shares, author, thumbnail, viral_score, created_at
        FROM videos
        WHERE analysis_id = ?
        ORDER BY viral_score DESC
    """, (analysis_id,))
    
    videos = []
    for row in cursor.fetchall():
        videos.append(
            VideoData(
                title=row[0],
                url=row[1],
                views=row[2],
                likes=row[3],
                comments=row[4],
                shares=row[5],
                author=row[6],
                thumbnail=row[7],
                viral_score=row[8],
                created_at=row[9]
            )
        )
    
    conn.close()
    
    return AnalysisResult(
        analysis_id=analysis_id,
        niche=niche,
        platform=platform,
        status=status,
        total_videos=total_videos,
        videos=videos,
        created_at=created_at
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

