"""
Agente de IA para geração de roteiros de conteúdo
Simulação de integração com LLM (OpenAI/Gemini) para MVP
"""

from typing import Dict, List
import random


def generate_content_script(title: str, llm_provider: str = "mock") -> Dict:
    """
    Gera um roteiro de conteúdo baseado em um título
    
    TODO: Integrar com OpenAI GPT-4 ou Gemini 2.5 Flash
    """
    
    if llm_provider == "mock":
        return _generate_mock_script(title)
    else:
        # Implementar integração real com LLM aqui
        return _generate_llm_script(title, llm_provider)


def _generate_mock_script(title: str) -> Dict:
    """
    Gera um roteiro mockado para desenvolvimento
    """
    
    # Templates de roteiros
    hook_templates = [
        f"Você já ouviu falar sobre {title}? Spoiler: isso vai mudar sua perspectiva.",
        f"Se você está procurando {title}, pare tudo agora! Este é o guia definitivo.",
        f"Prepare-se para descobrir os segredos por trás de {title} que ninguém te conta.",
    ]
    
    body_templates = [
        "Vamos começar com o básico: o que é e por que importa. Primeiro ponto, vamos falar sobre benefícios práticos. Segundo ponto, como implementar na sua rotina. Terceiro ponto, erros comuns a evitar.",
        "Dividi em três partes principais: conceito e fundamentos, aplicação prática, e dicas avançadas. Começando pela parte 1, você precisa entender os princípios básicos. Na parte 2, vou te mostrar passo a passo. Na parte 3, vou compartilhar segredos que profissionais usam.",
    ]
    
    cta_templates = [
        "Se esse conteúdo te ajudou, deixa um like e salva para não perder! Comenta aí embaixo o que você achou e me siga para mais dicas.",
        "Agora é com você! Coloca essas dicas em prática e me conta como foi nos comentários. Se gostou, compartilha com alguém que também vai adorar!",
    ]
    
    script_text = f"""
TÍTULO: {title}

HOOK (0:00-0:10)
{random.choice(hook_templates)}

DESENVOLVIMENTO (0:10-0:50)
{random.choice(body_templates)}

CTA (0:50-1:00)
{random.choice(cta_templates)}
"""
    
    structure = {
        "title": title,
        "hook": {
            "duration": "10 segundos",
            "tips": ["Criar curiosidade", "Prometer valor", "Conexão emocional"]
        },
        "body": {
            "duration": "40 segundos",
            "sections": [
                {"name": "Contexto", "time": "0:10-0:20"},
                {"name": "Conteúdo Principal", "time": "0:20-0:40"},
                {"name": "Exemplos Práticos", "time": "0:40-0:50"}
            ]
        },
        "cta": {
            "duration": "10 segundos",
            "actions": ["Like", "Comente", "Compartilhe", "Siga"]
        }
    }
    
    return {
        "script": script_text.strip(),
        "structure": structure
    }


def _generate_llm_script(title: str, provider: str) -> Dict:
    """
    Gera roteiro usando LLM real (OpenAI/Gemini)
    TODO: Implementar integração real
    """
    # Placeholder para implementação real
    pass


def analyze_content_trends(videos: List[Dict]) -> Dict:
    """
    Analisa tendências de conteúdo de uma lista de vídeos
    Extrai padrões comuns em títulos, estruturas e temas
    """
    
    # Extrair palavras-chave mais comuns dos títulos
    keywords = []
    for video in videos:
        title_words = video.get("title", "").lower().split()
        keywords.extend([word for word in title_words if len(word) > 3])
    
    # Contar frequência
    keyword_freq = {}
    for keyword in keywords:
        keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
    
    # Top 5 keywords
    top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Calcular métricas médias
    avg_views = sum(v.get("views", 0) for v in videos) / len(videos) if videos else 0
    avg_engagement = 0
    if all("likes" in v and v["likes"] for v in videos):
        avg_likes = sum(v.get("likes", 0) for v in videos) / len(videos)
        avg_views_rounded = avg_views if avg_views > 0 else 1
        avg_engagement = (avg_likes / avg_views_rounded) * 100
    
    return {
        "top_keywords": [{"word": word, "count": count} for word, count in top_keywords],
        "average_views": round(avg_views, 0),
        "average_engagement_rate": round(avg_engagement, 2),
        "total_videos_analyzed": len(videos)
    }

