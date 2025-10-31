"""
Cuga Agent - Frontend Streamlit
MVP de uma plataforma SaaS para análise de tendências de conteúdo TikTok e YouTube
"""

import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import sys
import os

# Configurações
API_BASE_URL = "http://localhost:8000"

# Configuração da página
st.set_page_config(
    page_title="Cuga Agent - Análise de Tendências",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .video-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .score-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .score-high {
        background-color: #d4edda;
        color: #155724;
    }
    .score-medium {
        background-color: #fff3cd;
        color: #856404;
    }
    .score-low {
        background-color: #f8d7da;
        color: #721c24;
    }
</style>
""", unsafe_allow_html=True)


# Função auxiliar para formatar números
def format_number(num):
    """Formata números grandes para exibição"""
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    return str(num)


# Função auxiliar para obter cor do score
def get_score_color(score):
    """Retorna a cor baseada no score"""
    if score >= 70:
        return "score-high"
    elif score >= 40:
        return "score-medium"
    else:
        return "score-low"


# Sidebar
with st.sidebar:
    st.title(" Cuga Agent")
    st.markdown("---")
    
    st.markdown("### Menu")
    
    page = st.radio(
        "Navegação",
        ["🏠 Início", "📈 Nova Análise", "📚 Histórico", "✍️ Gerar Roteiro"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("### ℹ️ Sobre")
    st.info("""
    **Cuga Agent MVP v1.0.0**
    
    Plataforma de análise de tendências de conteúdo para TikTok e YouTube.
    
    **Recursos:**
    - Análise de viralidade
    - Ranking inteligente
    - Geração de roteiros
    - Histórico de análises
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔗 Links")
    st.markdown("[📖 Documentação](./)")
    st.markdown("[🐛 Reportar Bug](./)")


# Página Inicial
if page == "🏠 Início":
    st.markdown('<h1 class="main-header">🎬 Cuga Agent</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Analise tendências de conteúdo e descubra o que está viralizando agora</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 TikTok")
        st.markdown("Análise completa de tendências com métricas detalhadas de engajamento")
    
    with col2:
        st.markdown("### 🎥 YouTube")
        st.markdown("Análise de tendências (funcionalidade limitada no MVP)")
    
    with col3:
        st.markdown("### 🤖 IA")
        st.markdown("Geração automática de roteiros baseados em tendências")
    
    st.markdown("---")
    
    st.markdown("### 🚀 Como Funciona")
    
    steps = """
    1. **Escolha um nicho**: Selecione o nicho de conteúdo que deseja analisar
    2. **Selecione a plataforma**: TikTok (completo) ou YouTube (limitado)
    3. **Analise**: Veja os vídeos mais virais rankeados por score inteligente
    4. **Gere roteiros**: Use nossa IA para criar roteiros baseados nas tendências
    """
    
    st.markdown(steps)
    
    st.markdown("---")
    
    st.markdown("### 📈 Nichos Populares")
    
    niches = ["tech", "fitness", "comedy", "education", "lifestyle"]
    
    cols = st.columns(5)
    for i, niche in enumerate(niches):
        with cols[i]:
            if st.button(f"🔍 {niche.title()}", key=f"niche_{niche}", use_container_width=True):
                st.session_state.selected_niche = niche
                st.session_state.change_page = "📈 Nova Análise"


# Página de Nova Análise
elif page == "📈 Nova Análise":
    st.title("📈 Nova Análise de Tendências")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        niche = st.text_input(
            "🔍 Nicho de Conteúdo",
            value=st.session_state.get("selected_niche", ""),
            placeholder="Ex: tech, fitness, comedy",
            help="Digite o nicho ou palavra-chave que deseja analisar"
        )
    
    with col2:
        platform = st.selectbox(
            "📱 Plataforma",
            ["tiktok", "youtube"],
            format_func=lambda x: "TikTok" if x == "tiktok" else "YouTube",
            help="TikTok: análise completa | YouTube: funcionalidade limitada no MVP"
        )
    
    limit = st.slider(
        "📊 Número de Vídeos",
        min_value=10,
        max_value=50,
        value=20,
        step=5,
        help="Quantos vídeos analisar"
    )
    
    st.markdown("---")
    
    if st.button("🚀 Analisar Tendências", use_container_width=True, type="primary"):
        if not niche:
            st.error("⚠️ Por favor, digite um nicho para analisar")
        else:
            with st.spinner(f"Analisando tendências de '{niche}' no {platform}..."):
                try:
                    response = requests.post(
                        f"{API_BASE_URL}/api/analyze",
                        json={
                            "niche": niche,
                            "platform": platform,
                            "limit": limit
                        },
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        st.session_state.current_analysis = data
                        st.success(f"✅ Análise concluída! {data['total_videos']} vídeos encontrados.")
                        st.rerun()
                    elif response.status_code == 403:
                        st.warning("⚠️ Você atingiu o limite de análises do seu plano. Faça upgrade para continuar!")
                    else:
                        st.error(f"❌ Erro: {response.json().get('detail', 'Erro desconhecido')}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Erro de conexão. Verifique se o backend está rodando em http://localhost:8000")
                except Exception as e:
                    st.error(f"❌ Erro: {str(e)}")
    
    # Exibir resultados
    if "current_analysis" in st.session_state:
        st.markdown("---")
        st.markdown("## 📊 Resultados da Análise")
        
        analysis = st.session_state.current_analysis
        
        # Estatísticas gerais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Vídeos", analysis['total_videos'])
        
        with col2:
            avg_score = sum(v['viral_score'] for v in analysis['videos']) / len(analysis['videos'])
            st.metric("Score Médio", f"{avg_score:.1f}")
        
        with col3:
            max_views = max(v['views'] for v in analysis['videos'])
            st.metric("Views Máximo", format_number(max_views))
        
        with col4:
            platform_display = "TikTok" if analysis['platform'] == "tiktok" else "YouTube"
            st.metric("Plataforma", platform_display)
        
        st.markdown("---")
        
        # Lista de vídeos
        st.markdown("### 🎬 Top Vídeos Virais")
        
        for idx, video in enumerate(analysis['videos'][:10], 1):
            with st.container():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    if video.get('thumbnail'):
                        st.image(video['thumbnail'], width=150)
                    else:
                        st.markdown("📹")
                
                with col2:
                    score_class = get_score_color(video['viral_score'])
                    st.markdown(f"""
                    <div class="video-card">
                        <h4>#{idx} {video['title']}</h4>
                        <span class="score-badge {score_class}">Score: {video['viral_score']:.1f}</span>
                        <p><strong>Autor:</strong> {video['author']}</p>
                        <p><strong>Views:</strong> {format_number(video['views'])} | 
                        {'<strong>Likes:</strong> ' + format_number(video['likes']) if video.get('likes') else ''}
                        {'| <strong>Comentários:</strong> ' + format_number(video['comments']) if video.get('comments') else ''}
                        </p>
                        <a href="{video['url']}" target="_blank">🔗 Ver Vídeo</a>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Download CSV
        st.markdown("---")
        
        df = pd.DataFrame(analysis['videos'])
        csv = df.to_csv(index=False)
        
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"analysis_{niche}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )


# Página de Histórico
elif page == "📚 Histórico":
    st.title("📚 Histórico de Análises")
    
    st.markdown("---")
    
    if st.button("🔄 Atualizar", use_container_width=True):
        pass
    
    try:
        response = requests.get(f"{API_BASE_URL}/api/analyses")
        
        if response.status_code == 200:
            data = response.json()
            analyses = data.get('analyses', [])
            
            if analyses:
                for analysis in analyses:
                    with st.expander(f"📊 {analysis['niche']} - {analysis['platform']} | {analysis['total_videos']} vídeos"):
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Plataforma", analysis['platform'].title())
                        
                        with col2:
                            st.metric("Vídeos", analysis['total_videos'])
                        
                        with col3:
                            st.metric("Status", analysis['status'].title())
                        
                        if st.button(f"Ver Detalhes", key=f"details_{analysis['analysis_id']}"):
                            with st.spinner("Carregando detalhes..."):
                                detail_response = requests.get(
                                    f"{API_BASE_URL}/api/analyses/{analysis['analysis_id']}"
                                )
                                if detail_response.status_code == 200:
                                    st.session_state.current_analysis = detail_response.json()
                                    st.rerun()
            else:
                st.info("📭 Nenhuma análise ainda. Comece analisando um nicho!")
        else:
            st.error("❌ Erro ao carregar histórico")
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Erro de conexão. Verifique se o backend está rodando.")
    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")


# Página de Gerar Roteiro
elif page == "✍️ Gerar Roteiro":
    st.title("✍️ Gerador de Roteiro com IA")
    
    st.markdown("---")
    
    st.markdown("### 💡 Instruções")
    st.info("Digite um título ou tema e nossa IA irá gerar um roteiro estruturado para você!")
    
    title = st.text_input(
        "📝 Título/Tema do Vídeo",
        placeholder="Ex: Como criar vídeos virais no TikTok",
        help="Descreva o conteúdo que deseja criar"
    )
    
    if st.button("✨ Gerar Roteiro", use_container_width=True, type="primary"):
        if not title:
            st.error("⚠️ Por favor, digite um título para o vídeo")
        else:
            with st.spinner("🤖 Gerando roteiro com IA..."):
                try:
                    response = requests.post(
                        f"{API_BASE_URL}/api/generate-script",
                        json={"title": title}
                    )
                    
                    if response.status_code == 200:
                        script_data = response.json()
                        
                        st.success("✅ Roteiro gerado com sucesso!")
                        
                        st.markdown("---")
                        st.markdown("## 📄 Seu Roteiro")
                        
                        # Exibir estrutura
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("### 📊 Estrutura")
                            
                            structure = script_data['structure']
                            
                            st.markdown(f"**Hook**: {structure['hook']['duration']}")
                            for tip in structure['hook']['tips']:
                                st.markdown(f"- {tip}")
                            
                            st.markdown(f"\n**Corpo**: {structure['body']['duration']}")
                            for section in structure['body']['sections']:
                                st.markdown(f"- {section['name']} ({section['time']})")
                            
                            st.markdown(f"\n**CTA**: {structure['cta']['duration']}")
                            for action in structure['cta']['actions']:
                                st.markdown(f"- {action}")
                        
                        with col2:
                            st.markdown("### ✍️ Texto Completo")
                            st.text_area(
                                "Roteiro",
                                value=script_data['script'],
                                height=300,
                                label_visibility="collapsed"
                            )
                        
                        # Download
                        st.download_button(
                            label="📥 Download TXT",
                            data=script_data['script'],
                            file_name=f"script_{title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error(f"❌ Erro: {response.json().get('detail', 'Erro desconhecido')}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Erro de conexão. Verifique se o backend está rodando.")
                except Exception as e:
                    st.error(f"❌ Erro: {str(e)}")


# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Cuga Agent MVP v1.0.0 | Desenvolvido com ❤️ para criadores de conteúdo</p>
</div>
""", unsafe_allow_html=True)

