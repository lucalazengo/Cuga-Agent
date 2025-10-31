# 📁 Estrutura do Projeto Cuga Agent MVP

Estrutura completa de arquivos e pastas do projeto.

## 🗂️ Árvore de Diretórios

```
Cuga Agent/
│
├── 📄 README.md                          # Documentação principal
├── 📄 DESENVOLVIMENTO_MVP.md             # Relatório de desenvolvimento
├── 📄 INICIO_RAPIDO.md                   # Guia rápido de início
├── 📄 ESTRUTURA_PROJETO.md               # Este arquivo
│
├──  run_backend.bat                    # Script backend Windows
├──  run_frontend.bat                   # Script frontend Windows
├──  run_backend.sh                     # Script backend Linux/Mac
├──  run_frontend.sh                    # Script frontend Linux/Mac
│
├── 📁 docs/                              # Documentação de planejamento
│   ├── analise_completa.md              # Análise completa do projeto
│   ├── arquitetura_solucao.md           # Arquitetura proposta
│   ├── custos_precificacao.md           # Custos e precificação
│   ├── viabilidade_tecnica.md           # Viabilidade técnica
│   ├── roadmap_desenvolvimento.md       # Roadmap de desenvolvimento
│   ├── research_findings.md             # Pesquisas realizadas
│   ├── www.flagsmith.com_blog...md      # Análise de custos SaaS
│   └── architecture (1).png             # Diagrama de arquitetura
│
└── 📁 src/                               # Código fonte
    │
    ├── 📁 backend/                       # Backend FastAPI
    │   ├── 📄 main.py                   # API principal (FastAPI)
    │   ├── 📄 api_collectors.py         # Coletores TikTok/YouTube
    │   ├── 📄 ranking_algorithm.py      # Algoritmo de ranking
    │   ├── 📄 ai_agent.py               # Agente IA de roteiros
    │   └── 📄 requirements.txt          # Dependências Python
    │
    └── 📁 frontend/                      # Frontend Streamlit
        ├── 📄 app.py                    # App principal (Streamlit)
        ├── 📄 requirements.txt          # Dependências Python
        └── 📄 README.md                 # Documentação frontend
│
└──  cuga_agent.db                      # Banco SQLite (gerado)
```

##  Detalhamento por Módulo

### Backend (`src/backend/`)

#### `main.py` (API Principal)
- ✅ FastAPI application
- ✅ Endpoints RESTful
- ✅ Banco de dados SQLite
- ✅ Middleware CORS
- ✅ Modelos Pydantic
- ✅ Inicialização automática

**Endpoints:**
- `GET /` - Status
- `GET /health` - Health check
- `POST /api/analyze` - Análise de tendências
- `POST /api/generate-script` - Geração de roteiro
- `GET /api/analyses` - Listar análises
- `GET /api/analyses/{id}` - Detalhes de análise

#### `api_collectors.py` (Coletores de Dados)
- ✅ Coleta TikTok (simulado)
- ✅ Coleta YouTube (simulado)
- ✅ Geração de dados realistas
- ✅ Preparado para APIs reais

#### `ranking_algorithm.py` (Algoritmo)
- ✅ Score TikTok completo
- ✅ Score YouTube simplificado
- ✅ Fatores de viralidade
- ✅ Normalização de valores

#### `ai_agent.py` (Agente IA)
- ✅ Geração de roteiros
- ✅ Templates inteligentes
- ✅ Estrutura Hook/Body/CTA
- ✅ Preparado para LLM real

### Frontend (`src/frontend/`)

#### `app.py` (App Principal)
**Páginas:**
1. 🏠 **Início** - Landing page
2. 📈 **Nova Análise** - Busca de tendências
3. 📚 **Histórico** - Análises anteriores
4. ✍️ **Gerar Roteiro** - IA de roteiros

**Recursos:**
- ✅ Layout responsivo
- ✅ Visualização de dados
- ✅ Cards de vídeos
- ✅ Badges de score
- ✅ Download CSV
- ✅ Estatísticas gerais

### Documentação (`docs/`)

#### Fase de Planejamento
- `analise_completa.md` - Análise completa (646 linhas)
- `arquitetura_solucao.md` - Stack técnico
- `custos_precificacao.md` - Modelo de negócio
- `viabilidade_tecnica.md` - Viabilidade
- `roadmap_desenvolvimento.md` - Roadmap
- `research_findings.md` - Pesquisas

### Scripts de Execução

#### Windows
- `run_backend.bat` - Backend (setup + execução)
- `run_frontend.bat` - Frontend (setup + execução)

#### Linux/Mac
- `run_backend.sh` - Backend (setup + execução)
- `run_frontend.sh` - Frontend (setup + execução)

## Estatísticas do Projeto

### Backend
- **Arquivos:** 4 Python + 1 TXT
- **Linhas de código:** ~800
- **Endpoints:** 6
- **Tabelas DB:** 3

### Frontend
- **Arquivos:** 2 Python + 1 MD
- **Linhas de código:** ~500
- **Páginas:** 4
- **Componentes:** 10+

### Documentação
- **Arquivos:** 9 Markdown
- **Total:** ~2000 linhas
- **Cobertura:** 100%

### Total
- **Arquivos código:** 11
- **Linhas código:** ~1300
- **Documentação:** 9 arquivos
- **Scripts:** 4

## Dependências

### Backend (`requirements.txt`)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
```

### Frontend (`requirements.txt`)
```
streamlit==1.29.0
requests==2.31.0
pandas==2.1.4
```

## Módulos Implementados

### ✅ Core Features
- [x] API RESTful completa
- [x] Frontend Streamlit
- [x] Banco de dados
- [x] Algoritmo de ranking
- [x] Geração de roteiros
- [x] Visualização de dados

### ✅ Sistema
- [x] Inicialização automática
- [x] Migrações de banco
- [x] Validação de dados
- [x] Error handling
- [x] Logging básico

### ✅ UX/UI
- [x] Interface intuitiva
- [x] Navegação clara
- [x] Feedback visual
- [x] Responsividade
- [x] Exportação de dados

### ✅ Documentação
- [x] README principal
- [x] Relatório de desenvolvimento
- [x] Guia rápido
- [x] Comentários no código
- [x] Estrutura do projeto

## Próximos Arquivos (Roadmap)

### Integrações
```
src/backend/
├── config.py                      # Configurações centralizadas
├── auth.py                        # Autenticação JWT
├── openai_client.py               # Cliente OpenAI
├── manus_api_client.py            # Cliente Manus API
└── .env                           # Variáveis de ambiente
```

### Melhorias
```
src/backend/
├── cache.py                       # Cache Redis
├── celery_app.py                  # Workers Celery
├── migrations/                    # Migrações PostgreSQL
└── tests/                         # Testes automatizados

src/frontend/
├── components/                    # Componentes reutilizáveis
├── utils/                         # Utilitários
└── config.py                      # Configurações
```

### Produção
```
├── docker-compose.yml             # Orquestração
├── Dockerfile.backend             # Container backend
├── Dockerfile.frontend            # Container frontend
├── .github/workflows/             # CI/CD
├── nginx.conf                     # Proxy reverso
└── kubernetes/                    # Deploy K8s
```

## Notas de Desenvolvimento

### Convenções
- Python 3.8+ com type hints
- Pydantic models para validação
- Async/await quando necessário
- Docstrings em funções
- Commentários explicativos

### Estrutura de Arquivos
- Módulos separados por responsabilidade
- Imports organizados
- Código limpo e legível
- Preparado para testes

### Versionamento
- MVP v1.0.0
- Compatível com evolução
- Breaking changes documentados
- Changelog recomendado

## Como Navegar

### Para Desenvolvedores
1. Leia `README.md` - Visão geral
2. Veja `DESENVOLVIMENTO_MVP.md` - Detalhes técnicos
3. Explore `src/backend/main.py` - Comece pela API
4. Veja `src/frontend/app.py` - Interface

### Para Usuários
1. Leia `INICIO_RAPIDO.md` - Guia rápido
2. Siga os scripts de execução
3. Explore as funcionalidades
4. Consulte documentação quando necessário

### Para Stakeholders
1. Leia `docs/analise_completa.md` - Visão geral
2. Veja `DESENVOLVIMENTO_MVP.md` - Status
3. Consulte `docs/roadmap_desenvolvimento.md` - Futuro
4. Analise métricas e KPIs

---

Create by **m1m2**. 

