# Arquitetura da Solução e Stack Tecnológico

## 1. Visão Geral da Arquitetura

A arquitetura proposta para a plataforma SaaS de sugestão de conteúdos é baseada em um sistema de microserviços desacoplado, projetado para escalabilidade, resiliência e manutenibilidade. A solução separa a interface do usuário (Frontend), a lógica de negócio (Backend), a coleta de dados e a análise em componentes independentes que se comunicam através de APIs e filas de mensagens.

### Diagrama da Arquitetura

O diagrama abaixo ilustra os principais componentes da solução e suas interações:

![Arquitetura da Solução SaaS](/home/ubuntu/architecture.png)

## 2. Componentes da Arquitetura

| Componente | Tecnologia Sugerida | Responsabilidade |
| :--- | :--- | :--- |
| **Frontend** | Next.js (React) | Interface do usuário, visualização de dados, dashboards interativos. |
| **Backend API** | FastAPI (Python) | Ponto de entrada para o frontend, gerenciamento de usuários, orquestração de tarefas. |
| **Banco de Dados** | PostgreSQL | Armazenamento de dados de usuários, vídeos, métricas e resultados de análises. |
| **Cache & Fila** | Redis | Cache de resultados de API para performance e sistema de filas para tarefas assíncronas. |
| **Worker de Coleta** | Celery (Python) | Tarefa assíncrona responsável por chamar APIs externas (YouTube, TikTok) e coletar dados. |
| **Worker de Análise** | Celery (Python) | Tarefa assíncrona que processa os dados brutos, calcula scores de viralidade e rankeia conteúdos. |
| **Agente IA** | LangChain / Custom | Módulo de IA para gerar roteiros e sugestões de conteúdo, utilizando um LLM externo. |
| **APIs de Dados** | Manus Data APIs | Fonte externa para os dados de tendências do YouTube e TikTok. |
| **API de LLM** | OpenAI / Gemini | Modelo de linguagem para a geração de texto do agente de roteiros. |

## 3. Justificativa do Stack Tecnológico

### Frontend: Next.js (React)
- **Renderização Híbrida (SSR/SSG):** Permite páginas rápidas e otimizadas para SEO, essencial para um SaaS.
- **Ecossistema Robusto:** Ampla disponibilidade de bibliotecas de componentes (ex: Material UI, Shadcn) e ferramentas de visualização de dados (ex: Recharts, Nivo).
- **Experiência do Desenvolvedor:** Hot-reloading, sistema de arquivos para roteamento e uma comunidade forte facilitam o desenvolvimento rápido.

### Backend: FastAPI (Python)
- **Alta Performance:** É um dos frameworks web Python mais rápidos, ideal para servir como uma API de alto desempenho.
- **Desenvolvimento Rápido:** Utiliza type hints do Python para validação automática de dados, documentação de API (Swagger/OpenAPI) e auto-complete, reduzindo bugs e acelerando o desenvolvimento.
- **Ecossistema Python:** Perfeita integração com o restante do stack de dados (Celery, Pandas, bibliotecas de IA), permitindo o reuso de modelos de dados e lógica de negócio.

### Banco de Dados: PostgreSQL
- **Confiabilidade e Robustez:** Transacional (ACID) e extremamente confiável para dados relacionais como usuários, vídeos e métricas associadas.
- **Flexibilidade:** Suporte nativo a tipos de dados complexos como JSONB, permitindo armazenar dados semi-estruturados (respostas de API) de forma eficiente sem a necessidade de um banco NoSQL separado no início.
- **Escalabilidade:** Comprovado em produção em larga escala e com extensões poderosas como TimescaleDB (para séries temporais) caso a análise de tendências se torne mais complexa.

### Cache e Fila: Redis
- **Versatilidade:** Serve tanto como um cache de altíssima velocidade para aliviar o banco de dados e as APIs externas, quanto como um message broker para o Celery, simplificando a infraestrutura.
- **Performance:** Operações em memória garantem latência extremamente baixa para caching e enfileiramento de tarefas.

### Workers Assíncronos: Celery
- **Processamento em Background:** Essencial para tarefas demoradas como coleta de dados de APIs externas e processamento de análises, evitando que a API principal fique bloqueada e garantindo uma boa experiência ao usuário.
- **Escalabilidade Horizontal:** Permite escalar o número de workers de coleta e análise de forma independente, conforme a carga de trabalho aumenta.

## 4. Fluxo de Dados e Processamento

1. O **Usuário**, através do **Frontend**, solicita uma análise de tendências para um nicho (ex: "tech").
2. O **Backend API** recebe a requisição, autentica o usuário e enfileira uma nova tarefa de coleta no **Redis**.
3. Um **Worker de Coleta (Celery)** consome a tarefa da fila, chama as para buscar vídeos em alta no TikTok e YouTube.
4. Os dados brutos coletados são salvos no **PostgreSQL**.
5. Ao final da coleta, o worker enfileira uma tarefa de análise no **Redis**.
6. Um **Worker de Análise (Celery)** consome a tarefa, lê os dados brutos do **PostgreSQL**, aplica o algoritmo de ranking e salva os scores e insights de volta no banco de dados.
7. O **Frontend** consulta o **Backend API** periodicamente para verificar o status da tarefa. Quando finalizada, os resultados são exibidos no dashboard.
8. Se o usuário solicitar um roteiro, o **Backend** chama o **Agente IA**, que por sua vez utiliza um **LLM externo** para gerar o conteúdo e retorná-lo ao usuário.
