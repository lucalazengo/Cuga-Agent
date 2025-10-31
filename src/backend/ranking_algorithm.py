"""
Algoritmo de cálculo de score de viralidade
Baseado na documentação do projeto
"""

from typing import Dict, Optional
from datetime import datetime


def calculate_viral_score(video: Dict, platform: str) -> float:
    """
    Calcula o score de viralidade de um vídeo
    
    TikTok: Score completo com views, likes, comentários, compartilhamentos
    YouTube: Score simplificado apenas com views (limitado por APIs não-oficiais)
    """
    
    if platform == "tiktok":
        return _calculate_tiktok_score(video)
    elif platform == "youtube":
        return _calculate_youtube_score(video)
    else:
        return 0.0


def _calculate_tiktok_score(video: Dict) -> float:
    """
    Score de viralidade para TikTok (completo)
    
    Fórmula:
    Score = (Views × 0.3) + (Likes × 0.25) + (Comentários × 0.20) + 
            (Compartilhamentos × 0.15) + (Taxa de Engajamento × 0.10)
    
    Taxa de Engajamento = (Likes + Comentários + Compartilhamentos) / Views
    """
    views = video.get("views", 0)
    likes = video.get("likes", 0) or 0
    comments = video.get("comments", 0) or 0
    shares = video.get("shares", 0) or 0
    
    # Normalizar valores para evitar que números muito grandes dominem
    views_score = min(views / 1000000, 1.0)  # Máximo 1M views = 1.0
    likes_score = min(likes / 100000, 1.0)  # Máximo 100K likes = 1.0
    comments_score = min(comments / 10000, 1.0)  # Máximo 10K comments = 1.0
    shares_score = min(shares / 50000, 1.0)  # Máximo 50K shares = 1.0
    
    # Calcular taxa de engajamento
    if views > 0:
        engagement_rate = (likes + comments + shares) / views
        # Normalizar taxa de engajamento (0-1, onde >0.2 é muito bom)
        engagement_score = min(engagement_rate / 0.2, 1.0)
    else:
        engagement_score = 0.0
    
    # Fator de recência (vídeos mais recentes ganham mais peso)
    recency_score = _calculate_recency_score(video.get("created_at"))
    
    # Calcular score final
    viral_score = (
        views_score * 0.25 +
        likes_score * 0.25 +
        comments_score * 0.20 +
        shares_score * 0.15 +
        engagement_score * 0.10 +
        recency_score * 0.05
    ) * 100
    
    # Multiplicar por 100 para ter scores de 0-100
    return round(viral_score, 2)


def _calculate_youtube_score(video: Dict) -> float:
    """
    Score de viralidade para YouTube (simplificado)
    
    Fórmula:
    Score = (Views × 0.6) + (Recência × 0.2) + (Fator de Canal × 0.2)
    
    Limitação: Sem dados de likes/comentários nas APIs não-oficiais
    """
    views = video.get("views", 0)
    
    # Normalizar views (YouTube tem números maiores)
    views_score = min(views / 5000000, 1.0)  # Máximo 5M views = 1.0
    
    # Fator de recência
    recency_score = _calculate_recency_score(video.get("created_at"))
    
    # Fator de canal (simulado - em produção seria baseado em histórico do canal)
    # Para MVP, vamos usar um fator fixo
    channel_score = 0.5  # Placeholder
    
    # Calcular score final
    viral_score = (
        views_score * 0.6 +
        recency_score * 0.2 +
        channel_score * 0.2
    ) * 100
    
    return round(viral_score, 2)


def _calculate_recency_score(created_at: Optional[str]) -> float:
    """
    Calcula score de recência
    Vídeos mais recentes têm score maior
    """
    if not created_at:
        return 0.5  # Score neutro se não houver data
    
    try:
        created_time = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        now = datetime.now(created_time.tzinfo) if created_time.tzinfo else datetime.now()
        
        # Calcular horas desde a criação
        time_diff = now - created_time
        hours_ago = time_diff.total_seconds() / 3600
        
        # Score decai com o tempo
        # 0-24h: 1.0, 24-48h: 0.8, 48-72h: 0.6, 72-168h: 0.4, >168h: 0.2
        if hours_ago <= 24:
            return 1.0
        elif hours_ago <= 48:
            return 0.8
        elif hours_ago <= 72:
            return 0.6
        elif hours_ago <= 168:  # 7 dias
            return 0.4
        else:
            return 0.2
            
    except Exception:
        return 0.5  # Score neutro em caso de erro


def format_score(score: float) -> str:
    """Formata o score para exibição"""
    return f"{score:.1f}"

