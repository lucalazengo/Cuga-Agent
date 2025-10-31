# Descobertas Iniciais - Pesquisa de APIs e Ferramentas

## APIs Disponíveis

### YouTube APIs
1. **Search Youtube** - Buscar vídeos por palavras-chave com métricas (views, título, descrição)
2. **Get Youtube Channel Videos** - Obter lista de vídeos de um canal com metadados (views, duração, publicação)
3. **Get Youtube Channel Details** - Informações detalhadas do canal (estatísticas, descrição, tags)

**Limitação importante**: As APIs disponíveis fornecem views, mas NÃO fornecem likes e comentários diretamente.

### TikTok APIs
1. **Search Tiktok video** - Buscar vídeos top por palavras-chave (inclui likes, views, comentários)
2. **Get TikTok user's popular posts** - Posts populares de influenciadores específicos
3. **Get TikTok basic user information** - Informações básicas de usuários

**Vantagem**: APIs do TikTok fornecem métricas de engajamento completas (likes, views, comentários).

## Ferramentas de Análise de Tendências (Mercado)

### Ferramentas Especializadas
- **TickerTrends** - Plataforma de inteligência de tendências TikTok
- **quso.ai** - Score de viralidade AI para Shorts, Reels e TikToks
- **ViralStat** - Plataforma de analytics cross-platform
- **Viral Predictor** - Testes A/B e análise de conteúdo viral
- **StreamLadder** - Score de viralidade AI
- **BuzzSumo** - Análise de conteúdo e identificação de tópicos populares
- **TrendTok** - Rastreamento de tendências e hashtags

### Ferramentas Generalistas
- **Hootsuite, Buffer, Sprout Social** - Analytics de vídeo em redes sociais
- **Google Trends** - Análise de tendências de pesquisa

## Próximos Passos
1. Testar APIs para verificar qualidade e completude dos dados
2. Analisar limitações técnicas (rate limits, custos)
3. Pesquisar sobre YouTube Data API oficial vs APIs não-oficiais
4. Investigar alternativas para obter métricas completas do YouTube


## YouTube Data API - Custos de Quota

### Quota Padrão
- **10.000 unidades por dia** (gratuito)
- Reset diário à meia-noite Pacific Time (PT)
- Possível solicitar aumento de quota (mas requer aprovação do Google)

### Custos por Operação (em unidades de quota)
- **search.list**: 100 unidades (busca de vídeos)
- **videos.list**: 1 unidade (obter detalhes de vídeos, incluindo estatísticas)
- **comments.list**: 1 unidade (listar comentários)
- **commentThreads.list**: 1 unidade (listar threads de comentários)
- **channels.list**: 1 unidade (informações do canal)

### Implicações para o Projeto
Com quota padrão de 10.000 unidades/dia:
- **100 buscas** por dia (search.list = 100 unidades cada)
- OU **10.000 consultas** de detalhes de vídeos (videos.list = 1 unidade cada)
- OU combinação proporcional

**Problema**: Para uma aplicação SaaS com múltiplos usuários, 10.000 unidades/dia é **extremamente limitado**.

### Exemplo de Uso Real
Se um usuário quiser analisar 50 vídeos em alta:
1. 1 busca (100 unidades) = retorna lista de vídeos
2. 50 chamadas videos.list (50 unidades) = obter estatísticas completas
3. **Total: 150 unidades por análise**

Com 10.000 unidades/dia: **~66 análises por dia para TODOS os usuários**

### Solução para Escalar
1. **Solicitar aumento de quota** ao Google (pode chegar a milhões, mas requer justificativa)
2. **Usar APIs não-oficiais** (como as disponíveis no Manus) que não têm essas limitações
3. **Implementar cache agressivo** para reduzir chamadas repetidas
4. **Modelo híbrido**: APIs não-oficiais para coleta + YouTube Data API oficial apenas quando necessário


## Custos de Infraestrutura SaaS - Caso Real (Flagsmith)

### Evolução de Custos por Escala

**Fase 1 - MVP (20 milhões de requisições/mês)**
- Custo: ~$40/mês
- Infraestrutura: Servidor Hetzner + Dokku (auto-hospedado)
- Limitações: Sem redundância, backup limitado, ponto único de falha

**Fase 2 - Crescimento (600 milhões de requisições/mês)**
- Custo: $300-$800/mês
- Infraestrutura: AWS Elastic Beanstalk + RDS Postgres + CloudFront
- Observação: CloudFront (CDN) é caro e inevitável para performance global

**Fase 3 - Escala (bilhões de requisições/mês)**
- Custo: ~$1.200/mês
- Infraestrutura: AWS ECS + Fargate + RDS + CloudFront
- Distribuição: 1/3 RDS, 1/3 ECS, 1/3 CloudFront/Bandwidth
- Melhoria: Custo por requisição DIMINUIU com escala

### Insights Importantes

1. **Problema B2B2C**: Um único cliente pode multiplicar o tráfego por 10x instantaneamente
2. **Custos de CDN**: CloudFront/Bandwidth representam ~33% dos custos totais
3. **Banco de dados**: Conexões concorrentes tornam-se gargalo antes do servidor de aplicação
4. **Escala reduz custo unitário**: Com infraestrutura moderna, custo por requisição diminui ao escalar

### Estimativa para o Projeto

Para um SaaS de análise de tendências com 1.000 usuários ativos:
- **Coleta de dados**: 10.000 vídeos analisados/dia
- **Processamento**: Análise de métricas + ranking + IA para sugestões
- **Armazenamento**: Histórico de tendências + cache de resultados

**Estimativa conservadora**: $500-$2.000/mês para começar (100-1.000 usuários)
**Estimativa em escala**: $3.000-$10.000/mês (10.000+ usuários)

Componentes principais de custo:
- **Banco de dados** (PostgreSQL/MongoDB): 30-40%
- **Servidores de aplicação** (ECS/Kubernetes): 30-40%
- **CDN e bandwidth**: 20-30%
- **APIs de terceiros**: Variável (pode ser zero com APIs não-oficiais)
