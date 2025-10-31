#  Cuga Agent - MVP

Plataforma SaaS de análise de tendências de conteúdo para TikTok e YouTube com IA para geração de roteiros.

##  Visão Geral

O **Cuga Agent** é uma solução MVP para criadores de conteúdo que desejam:
- 📊 Analisar tendências virais em tempo real
- 🎯 Identificar nichos promissores
- 🤖 Gerar roteiros inteligentes com IA
- 📈 Monitorar performance de conteúdo

## Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                     FRONTEND                            │
│                  Streamlit (MVP)                        │
│  Dashboard | Análise | Histórico | Gerador de Roteiros │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                     BACKEND API                         │
│                     FastAPI                             │
│     /api/analyze | /api/generate-script | /analyses    │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   COMPONENTES DE NEGÓCIO     │
        ├──────────────────────────────┤
        │ • API Collectors (TikTok/Youtube) │
        │ • Ranking Algorithm (Viral Score)  │
        │ • AI Agent (Script Generator)      │
        └──────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   BANCO DE DADOS             │
        │   SQLite (MVP)               │
        │   PostgreSQL (Produção)      │
        └──────────────────────────────┘
```

##  Como Rodar

### Pré-requisitos

- Python 3.8+
- pip

### Instalação e Execução

#### 1. Backend (API)

```bash
# Navegar para pasta backend
cd src/backend

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python main.py
# ou
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

O backend estará disponível em: http://localhost:8000

**Documentação da API:** http://localhost:8000/docs

#### 2. Frontend (Streamlit)

Em um novo terminal:

```bash
# Navegar para pasta frontend
cd src/frontend

# Criar ambiente virtual (se ainda não tiver)
python -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar aplicação
streamlit run app.py
```

O frontend estará disponível em: http://localhost:8501

## 📁 Estrutura do Projeto

```
Cuga Agent/
├── docs/                          # Documentação do projeto
│   ├── analise_completa.md       # Análise completa
│   ├── arquitetura_solucao.md    # Arquitetura proposta
│   ├── viabilidade_tecnica.md    # Viabilidade técnica
│   ├── custos_precificacao.md    # Custos e precificação
│   ├── roadmap_desenvolvimento.md # Roadmap
│   └── ...
├── src/
│   ├── backend/                   # Backend FastAPI
│   │   ├── main.py               # API principal
│   │   ├── api_collectors.py     # Coletas TikTok/YouTube
│   │   ├── ranking_algorithm.py  # Algoritmo de ranking
│   │   ├── ai_agent.py           # Agente IA
│   │   └── requirements.txt      # Dependências
│   └── frontend/                  # Frontend Streamlit
│       ├── app.py                # App principal
│       ├── requirements.txt      # Dependências
│       └── README.md             # Documentação
├── cuga_agent.db                  # Banco de dados SQLite (gerado)
└── README.md                      # Este arquivo
```

##  Funcionalidades MVP

### ✅ Implementadas

1. **Backend API com FastAPI**
   - Endpoints RESTful completos
   - Sistema de autenticação demo
   - Gerenciamento de análises
   - Banco de dados SQLite

2. **Coletores de Dados**
   - Integração com APIs TikTok (simulada)
   - Integração com APIs YouTube (simulada)
   - Extração de métricas de engajamento

3. **Algoritmo de Ranking**
   - Score de viralidade para TikTok (completo)
   - Score de viralidade para YouTube (limitado)
   - Fatores: views, likes, comentários, compartilhamentos, recência

4. **Frontend Streamlit**
   - Dashboard interativo
   - Análise de tendências
   - Visualização de resultados
   - Histórico de análises

5. **Agente IA**
   - Geração de roteiros simples
   - Estrutura: Hook, Desenvolvimento, CTA
   - Sistema mockado (preparado para integração LLM real)

##  Próximos Passos

### Fase 1 - Integrações Reais
- [ ] Integrar APIs Manus Data TikTok/YouTube reais
- [ ] Integrar OpenAI GPT-4 ou Gemini para roteiros
- [ ] Implementar autenticação real (JWT/OAuth)
- [ ] Migrar para PostgreSQL

### Fase 2 - Melhorias
- [ ] Implementar cache Redis
- [ ] Adicionar workers Celery para processamento assíncrono
- [ ] Dashboard com gráficos e métricas avançadas
- [ ] Sistema de alertas de tendências

### Fase 3 - Escala
- [ ] Implementar planos freemium/starter/pro
- [ ] Integração com Stripe para pagamentos
- [ ] API pública para clientes Enterprise
- [ ] Análise de concorrentes
- [ ] Exportação PDF

##  Tecnologias Utilizadas

**Backend:**
- FastAPI - Framework web moderno
- SQLite - Banco de dados MVP
- Pydantic - Validação de dados
- Uvicorn - Servidor ASGI

**Frontend:**
- Streamlit - Framework para dashboards
- Requests - Cliente HTTP
- Pandas - Manipulação de dados

**Próximas:**
- PostgreSQL - Banco de dados produção
- Redis - Cache e filas
- Celery - Workers assíncronos
- OpenAI/Gemini - LLM

##  Configuração

### Variáveis de Ambiente

Criar arquivo `.env` no backend com:

```env
# API Keys (quando disponíveis)
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
MANUS_API_KEY=...

# Database
DATABASE_PATH=cuga_agent.db

# Server
HOST=0.0.0.0
PORT=8000
```

##  Licença

Este é um projeto MVP desenvolvido para demonstração.

##  Contribuição

Este é um MVP em desenvolvimento. Sugestões e melhorias são bem-vindas!


Create by **m1m2**. 


