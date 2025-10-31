"""
Coletores de dados para TikTok e YouTube
Simulação das APIs Manus Data para desenvolvimento
"""

from typing import List, Dict
import random
from datetime import datetime, timedelta


def collect_tiktok_data(niche: str, limit: int = 20) -> List[Dict]:
    """
    Coleta dados de vídeos TikTok por nicho
    TODO: Integrar com API Manus Data TikTok quando disponível
    """
    # Dados de exemplo para desenvolvimento
    sample_videos = []
    
    # Nichos comuns e títulos de exemplo
    niche_keywords = {
        "tech": ["iPhone 16", "MacBook Pro", "AI Revolution", "Gaming Setup"],
        "fitness": ["Morning Workout", "Gym Transformation", "Diet Tips", "Yoga Flow"],
        "comedy": ["Prank Fail", "Funny Moments", "Reaction Video", "Comedy Skit"],
        "education": ["Study Tips", "Math Tutorial", "History Explained", "Science Facts"],
        "lifestyle": ["Morning Routine", "Room Tour", "GRWM", "Day in My Life"]
    }
    
    keywords = niche_keywords.get(niche.lower(), ["Trending Video", "Viral Content", "Must Watch"])
    
    for i in range(limit):
        keyword = random.choice(keywords)
        
        # Gerar métricas realistas
        views = random.randint(10000, 5000000)
        likes = int(views * random.uniform(0.05, 0.15))
        comments = int(views * random.uniform(0.01, 0.03))
        shares = int(views * random.uniform(0.005, 0.02))
        
        # Timestamp recente
        hours_ago = random.randint(1, 168)  # Últimas 7 dias
        created_at = (datetime.now() - timedelta(hours=hours_ago)).isoformat()
        
        video_data = {
            "title": f"{keyword} - {i+1}",
            "url": f"https://www.tiktok.com/@creator{i}/video/{random.randint(1000000000, 9999999999)}",
            "views": views,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "author": f"@creator{i}",
            "thumbnail": f"https://picsum.photos/seed/{i}/400/600",
            "created_at": created_at
        }
        
        sample_videos.append(video_data)
    
    return sample_videos


def collect_youtube_data(niche: str, limit: int = 20) -> List[Dict]:
    """
    Coleta dados de vídeos YouTube por nicho
    TODO: Integrar com API Manus Data YouTube quando disponível
    """
    # Dados de exemplo para desenvolvimento
    sample_videos = []
    
    # Nichos comuns e títulos de exemplo
    niche_keywords = {
        "tech": ["Latest Gadget Review", "Tech News 2025", "App Tutorial", "Hardware Unboxing"],
        "fitness": ["Workout Challenge", "Fitness Journey", "Nutrition Guide", "Yoga Session"],
        "comedy": ["Funny Compilation", "Comedy Sketch", "Reaction Time", "Pranks Gone Wrong"],
        "education": ["How to Learn", "Study Techniques", "Science Explained", "History Deep Dive"],
        "lifestyle": ["Productivity Tips", "Room Decor Ideas", "Travel Vlog", "Shopping Haul"]
    }
    
    keywords = niche_keywords.get(niche.lower(), ["Trending Video", "Viral Content", "Must Watch"])
    
    for i in range(limit):
        keyword = random.choice(keywords)
        
        # Gerar métricas realistas (mais views, sem likes/comments)
        views = random.randint(100000, 10000000)
        
        # Timestamp recente
        hours_ago = random.randint(1, 336)  # Últimas 2 semanas
        created_at = (datetime.now() - timedelta(hours=hours_ago)).isoformat()
        
        video_data = {
            "title": f"{keyword} - {i+1}",
            "url": f"https://www.youtube.com/watch?v={random.randint(10000000000, 99999999999)}",
            "views": views,
            "likes": None,  # YouTube não tem nas APIs não-oficiais
            "comments": None,
            "shares": None,
            "author": f"YouTuber Channel {i}",
            "thumbnail": f"https://picsum.photos/seed/youtube{i}/800/450",
            "created_at": created_at
        }
        
        sample_videos.append(video_data)
    
    return sample_videos


def format_metric(value: int) -> str:
    """Formata números grandes para exibição"""
    if value >= 1000000:
        return f"{value/1000000:.1f}M"
    elif value >= 1000:
        return f"{value/1000:.1f}K"
    return str(value)

