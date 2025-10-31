#  Guia de Início Rápido - Cuga Agent

Guia rápido para rodar o Cuga Agent MVP em 5 minutos.

---

##  Início Ultra-Rápido

### Windows

```bash
# 1. Clonar/baixar o projeto
# 2. Abrir 2 terminais

# Terminal 1 - Backend
.\run_backend.bat

# Terminal 2 - Frontend (aguarde backend inicializar)
.\run_frontend.bat
```

### Linux/Mac

```bash
# 1. Clonar/baixar o projeto
# 2. Abrir 2 terminais

# Terminal 1 - Backend
chmod +x run_backend.sh
./run_backend.sh

# Terminal 2 - Frontend (aguarde backend inicializar)
chmod +x run_frontend.sh
./run_frontend.sh
```

---

##  Endereços

- **Frontend:** http://localhost:8501
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

---

##  Primeiros Passos

### 1. Testar a API

Abra http://localhost:8000/docs no navegador.

Você verá a documentação interativa do Swagger. Teste:
- `GET /` - Status da API
- `GET /health` - Health check

### 2. Usar o Frontend

Abra http://localhost:8501 no navegador.

**Páginas disponíveis:**
- 🏠 **Início** - Visão geral
- 📈 **Nova Análise** - Analisar tendências
- 📚 **Histórico** - Ver análises anteriores
- ✍️ **Gerar Roteiro** - Criar roteiro com IA

### 3. Fazer Primeira Análise

1. Vá em "📈 Nova Análise"
2. Digite um nicho (ex: "tech", "fitness")
3. Selecione a plataforma (TikTok ou YouTube)
4. Clique em "🚀 Analisar Tendências"
5. Veja os resultados!

### 4. Gerar Primeiro Roteiro

1. Vá em " Gerar Roteiro"
2. Digite um título (ex: "Como criar vídeos virais")
3. Clique em "✨ Gerar Roteiro"
4. Veja o resultado!

---

##  Funcionalidades Disponíveis

### ✅ Implementado

- ✅ Análise de tendências TikTok (simulado)
- ✅ Análise de tendências YouTube (simulado)
- ✅ Score de viralidade
- ✅ Ranking inteligente
- ✅ Geração de roteiros
- ✅ Histórico de análises
- ✅ Exportação CSV
- ✅ Dashboard visual

###  Próximos

- ⏳ Integração com APIs reais
- ⏳ IA real (OpenAI/Gemini)
- ⏳ Autenticação de usuários
- ⏳ Planos premium
- ⏳ Gráficos avançados

---

##  Resolução de Problemas

### Backend não inicia

```bash
# Verificar Python
python --version  # Deve ser 3.8+

# Reinstalar dependências
cd src/backend
pip install -r requirements.txt -f

# Tentar manualmente
python main.py
```

### Frontend não inicia

```bash
# Reinstalar dependências
cd src/frontend
pip install -r requirements.txt -f

# Tentar manualmente
streamlit run app.py
```

### Erro de conexão

Verifique se:
1. Backend está rodando em http://localhost:8000
2. Porta 8000 não está em uso
3. Porta 8501 não está em uso

### Banco de dados

O SQLite é criado automaticamente. Se precisar resetar:

```bash
# Deletar banco antigo
rm cuga_agent.db  # Linux/Mac
del cuga_agent.db # Windows

# Iniciar backend novamente (cria novo banco)
```

---

##  Estrutura de Arquivos

```
Cuga Agent/
├── run_backend.bat      # Script backend Windows
├── run_frontend.bat     # Script frontend Windows
├── run_backend.sh       # Script backend Linux/Mac
├── run_frontend.sh      # Script frontend Linux/Mac
├── README.md            # Documentação principal
├── DESENVOLVIMENTO_MVP.md  # Relatório completo
├── INICIO_RAPIDO.md     # Este arquivo
├── src/
│   ├── backend/         # API FastAPI
│   └── frontend/        # App Streamlit
├── docs/                # Documentação do projeto
└── cuga_agent.db        # Banco SQLite (gerado)
```

---

##  Próximos Passos

1. ✅ **Explorar** o frontend
2. ✅ **Testar** análise de diferentes nichos
3. ✅ **Gerar** alguns roteiros
4. ✅ **Ler** a documentação completa
5. ✅ **Customizar** para suas necessidades

---

##  Ajuda

**Documentação:**
- `README.md` - Visão geral completa
- `DESENVOLVIMENTO_MVP.md` - Relatório de desenvolvimento
- `docs/` - Documentação técnica completa

**API:**
- http://localhost:8000/docs - Documentação interativa

---
Create by **m1m2**. 

