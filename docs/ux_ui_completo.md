# Fluxo de Navegação e Design de Interface - Agente de Conteúdo SaaS

## Introdução

Este documento apresenta uma proposta completa de experiência do usuário (UX) e interface do usuário (UI) para a plataforma SaaS de sugestão de conteúdos baseada em tendências do YouTube e TikTok. O design foi desenvolvido seguindo as melhores práticas da indústria, com foco em usabilidade, clareza, eficiência e escalabilidade.

A proposta abrange desde a definição de personas e jornadas do usuário até wireframes detalhados, especificações de componentes e diagramas de fluxo de navegação, fornecendo uma base sólida para o desenvolvimento da aplicação.

---

# 1. Personas e Jornadas do Usuário

## 1.1. Personas Principais

A plataforma foi projetada para atender três perfis principais de usuários, cada um com necessidades e comportamentos distintos.

### Persona 1: Criador de Conteúdo Individual

**Lucas, 28 anos**, é um criador de conteúdo focado em tecnologia que produz vídeos para TikTok e YouTube. Seu principal objetivo é crescer seu canal e aumentar o engajamento, mas ele enfrenta dificuldades em identificar quais tópicos estão em alta e têm maior potencial de viralização. Lucas acessa a plataforma duas a três vezes por semana para pesquisar tendências e gerar ideias de conteúdo. Ele valoriza interfaces simples e diretas, que o ajudem a encontrar insights rapidamente sem exigir conhecimento técnico avançado.

### Persona 2: Gestor de Agência de Marketing

**Marina, 35 anos**, trabalha como gestora em uma agência de marketing digital e é responsável por gerenciar a produção de conteúdo para múltiplos clientes em diferentes nichos. Sua principal dor é a necessidade de gerar insights rápidos e relatórios profissionais para apresentar aos clientes. Marina usa a plataforma diariamente, exporta dados em formatos como PDF e CSV, e compartilha análises com sua equipe. Ela precisa de funcionalidades avançadas como monitoramento de concorrentes e alertas automáticos de tendências.

### Persona 3: Empresa de Mídia

**Roberto, 42 anos**, é Diretor de Conteúdo de uma empresa de mídia que produz conteúdo em escala. Seu objetivo é identificar tendências de forma sistemática para orientar a produção de dezenas de vídeos por semana. Roberto necessita de análises profundas, integração com ferramentas internas via API e suporte para múltiplos usuários em sua equipe. Ele busca uma solução enterprise que ofereça confiabilidade, segurança e suporte dedicado.

## 1.2. Jornadas do Usuário

### Jornada 1: Primeiro Acesso (Novo Usuário)

O objetivo desta jornada é proporcionar um onboarding eficiente que demonstre o valor da plataforma rapidamente, minimizando a fricção e maximizando a taxa de ativação.

O usuário descobre a plataforma através da **Landing Page**, que comunica claramente a proposta de valor. Ao clicar em "Começar Grátis", ele é direcionado para um **formulário de cadastro** simplificado, com opções de registro via email/senha ou login social (Google, GitHub). Após o cadastro, o usuário passa por um **processo de onboarding** em três passos: primeiro, seleciona seu nicho principal (tech, beleza, fitness, etc.); segundo, escolhe as plataformas de interesse (TikTok, YouTube ou ambas); terceiro, tem a opção de fazer um tour guiado pela interface ou pular diretamente para o dashboard.

Ao chegar ao **Dashboard**, o sistema sugere automaticamente uma primeira análise baseada no nicho selecionado, permitindo que o usuário experimente o valor da plataforma imediatamente. Após visualizar os primeiros insights, um convite sutil para upgrade é apresentado, incentivando a conversão para planos pagos.

### Jornada 2: Análise de Tendências (Usuário Recorrente)

Esta jornada representa o fluxo principal de uso da plataforma, otimizado para permitir análises rápidas e eficientes.

O usuário faz login e acessa o **Dashboard**, onde visualiza uma visão geral de análises recentes e alertas de tendências. Ao clicar em **"Nova Análise"**, um modal de configuração é aberto, permitindo que ele insira uma palavra-chave ou tema, selecione a plataforma (TikTok ou YouTube) e defina o número de vídeos a analisar (20, 50 ou 100). Após confirmar, o sistema inicia o **processamento**, exibindo uma barra de progresso com mensagens contextuais e estimativa de tempo.

Quando a análise é concluída, o usuário é direcionado para a tela de **Resultados**, onde pode visualizar vídeos ranqueados com métricas detalhadas, gráficos de engajamento e insights gerados por IA. A partir daí, ele pode filtrar e ordenar os resultados, salvar a análise para consulta futura, exportar um relatório em PDF ou CSV, ou gerar um roteiro de vídeo baseado em um dos resultados.

### Jornada 3: Geração de Roteiro com IA

Esta jornada transforma insights em conteúdo prático, oferecendo um diferencial competitivo importante.

A partir da tela de **Resultados da Análise**, o usuário seleciona um vídeo de referência e clica em **"Gerar Roteiro com IA"**. Um modal de configuração é aberto, permitindo que ele defina o tipo de roteiro (TikTok curto, YouTube Short ou YouTube longo), o tom (educativo, divertido, inspirador), a duração estimada e se deseja incluir um CTA. Após confirmar, a IA processa a solicitação e gera um **roteiro estruturado** com seções claras (Gancho, Desenvolvimento, CTA), sugestões de B-roll e hashtags recomendadas.

O usuário pode editar o roteiro diretamente na interface, copiá-lo para a área de transferência, baixá-lo em formato .txt ou .docx, ou salvá-lo na seção "Meus Roteiros" para acesso futuro.

### Jornada 4: Monitoramento de Concorrentes (Plano Professional)

Esta funcionalidade premium permite que usuários acompanhem a estratégia de concorrentes de forma automatizada.

O usuário acessa a seção **"Concorrentes"** no menu lateral e clica em **"Adicionar Concorrente"**, inserindo a URL do canal que deseja monitorar. Ele define a frequência de análise (diária, semanal) e o sistema passa a coletar dados automaticamente. Quando o concorrente publica um vídeo que atinge métricas significativas, o usuário recebe um **alerta** por email ou notificação push. Na tela de **Análise Comparativa**, ele pode visualizar a performance de seus próprios vídeos em comparação com os concorrentes, identificando oportunidades e gaps de conteúdo.

---

# 2. Estrutura de Navegação e Wireframes

## 2.1. Arquitetura de Informação

A estrutura de navegação foi projetada para ser intuitiva e escalável, organizando as funcionalidades em uma hierarquia clara.

### Hierarquia de Navegação

A aplicação é dividida em duas grandes áreas: **Autenticação (Público)** e **Aplicação (Autenticado)**. A área pública inclui a Landing Page, telas de Login, Cadastro e Recuperação de Senha. A área autenticada é organizada em torno do Dashboard como ponto central, com acesso direto a:

- **Análises:** Nova Análise, Minhas Análises e Análise Detalhada
- **Roteiros:** Gerar Roteiro, Meus Roteiros e Editar Roteiro
- **Concorrentes (Professional+):** Lista de Concorrentes, Adicionar Concorrente e Análise Comparativa
- **Alertas (Professional+):** Configurar Alertas e Histórico de Alertas
- **Configurações:** Perfil, Plano e Faturamento, Notificações e Integrações (Enterprise)
- **Ajuda:** Documentação, Tutoriais em Vídeo e Suporte

## 2.2. Componentes de Navegação

### Navegação Principal (Sidebar)

A sidebar é o elemento de navegação primário da aplicação, sempre visível nas telas autenticadas. Ela é composta por três seções: no topo, o logo e nome da aplicação; no meio, o menu principal com ícones e labels; no rodapé, informações do usuário e indicador do plano atual.

Os itens do menu incluem Dashboard, Análises, Roteiros, Concorrentes (com badge "Pro"), Alertas (com badge "Pro"), Configurações e Ajuda. A sidebar é colapsável em dispositivos móveis, e o item ativo é destacado com a cor primária. Funcionalidades premium exibem badges visuais, e tooltips aparecem ao passar o mouse sobre os ícones na versão colapsada.

### Navegação Secundária (Top Bar)

A barra superior complementa a sidebar, oferecendo contexto e ações rápidas. À esquerda, um breadcrumb indica a localização atual do usuário na hierarquia de navegação. No centro, uma barra de busca global permite encontrar análises, roteiros e outros conteúdos rapidamente. À direita, encontram-se o botão de CTA primário "Nova Análise", um ícone de notificações e o avatar do usuário.

O dropdown do usuário, acessado ao clicar no avatar, exibe o nome, email e plano atual, além de links para Ver Perfil, Configurações, Upgrade (se aplicável) e Sair.

## 2.3. Wireframes das Telas Principais

### Landing Page

A Landing Page é projetada para converter visitantes em usuários, comunicando claramente a proposta de valor e facilitando o cadastro.

O cabeçalho contém o logo, menu de navegação (Funcionalidades, Preços) e botões de Login e "Começar". A seção hero apresenta um título impactante ("Descubra Tendências que Viralizam"), um subtítulo explicativo, um campo de email e um CTA proeminente "Começar Grátis". Abaixo, três ícones ilustram o funcionamento: "Insira Palavra-chave", "Análise IA Automática" e "Crie Conteúdo que Viraliza".

A seção de funcionalidades destaca os quatro pilares principais: Análise de Tendências, Roteiros com IA, Monitor de Concorrentes e Alertas em Tempo Real. A seção de preços apresenta os quatro planos (Freemium, Starter, Professional, Enterprise) em cards comparativos. Depoimentos de usuários reais aumentam a credibilidade, e o rodapé contém links institucionais e legais.

### Dashboard Principal

O Dashboard é o hub central da aplicação, oferecendo uma visão geral e acesso rápido às principais ações.

Uma saudação personalizada ("Olá, Lucas!") é seguida por um indicador de uso do plano ("Você tem 3 análises restantes este mês"). Dois cards de métricas exibem o número de análises e roteiros gerados no mês. A seção "Análises Recentes" lista as últimas análises realizadas, cada uma com título, plataforma, data e um botão "Ver Resultados".

Um card de "Tendências do Seu Nicho" mostra os tópicos em alta no nicho do usuário (ex: "AI Agents ↗️ +245%"), permitindo que ele identifique oportunidades rapidamente. Um botão CTA "Nova Análise" está posicionado de forma proeminente para facilitar a ação principal.

### Modal de Nova Análise

O modal de configuração de análise é simples e direto, minimizando a fricção para iniciar uma análise.

Um campo de texto permite inserir a palavra-chave ou tema (ex: "AI tools", "tech reviews"). Botões de rádio permitem selecionar a plataforma (TikTok, YouTube ou Ambas). O número de vídeos a analisar é configurável (20 para rápido, 50 recomendado, 100 para análise profunda). Uma seção colapsável de "Filtros Avançados" oferece opções adicionais para usuários mais experientes. Botões de "Cancelar" e "Analisar" finalizam o modal.

### Tela de Resultados da Análise

A tela de resultados é o coração da aplicação, apresentando insights de forma clara e acionável.

O cabeçalho exibe o título da análise, plataforma e metadados (data, número de vídeos). Botões de ação permitem salvar, exportar ou atualizar a análise. Um card de "Insights Principais" destaca padrões identificados pela IA (ex: "Vídeos curtos têm 2x mais engajamento", "Melhor horário: 18h-21h").

Filtros e opções de ordenação permitem refinar os resultados. Cada vídeo é apresentado em um card com thumbnail, título, autor, métricas (views, likes, comentários, compartilhamentos) e um score de viralidade visual (estrelas ou barra). Botões "Ver Detalhes" e "Gerar Roteiro" oferecem ações contextuais.

### Tela de Geração de Roteiro

A interface de geração de roteiro é dividida em duas colunas: configuração à esquerda e resultado à direita.

O painel de configuração permite selecionar o tipo de vídeo (TikTok, YouTube Short, YouTube Longo), o tom (educativo, divertido, inspirador) e opções adicionais (incluir B-roll, gerar hashtags, incluir CTA). O botão "Gerar Roteiro" inicia o processo.

O painel de resultado exibe o roteiro gerado de forma estruturada, com seções claramente marcadas (Gancho, Desenvolvimento, CTA). Sugestões de B-roll são inseridas inline, e hashtags recomendadas aparecem ao final. O usuário pode editar o texto diretamente, e botões permitem copiar, salvar ou gerar um novo roteiro.

### Tela de Configurações (Plano e Faturamento)

Esta tela oferece transparência e controle sobre a assinatura do usuário.

Um card destacado mostra o plano atual, preço, data de renovação e barras de progresso indicando o uso de análises e roteiros em relação ao limite do plano. As barras mudam de cor quando o uso se aproxima do limite (ex: amarelo acima de 80%).

Uma tabela comparativa apresenta todos os planos disponíveis, com o plano atual destacado. Botões contextuais permitem upgrade, downgrade ou gerenciamento da assinatura via Stripe. O histórico de faturas lista todas as transações com links para download em PDF.

---

# 3. Especificações de UI e Componentes

## 3.1. Princípios de Design

A interface foi projetada seguindo cinco princípios fundamentais que garantem uma experiência de usuário superior.

**Clareza e Simplicidade** são alcançadas através de uma hierarquia visual clara que guia o usuário sem sobrecarregá-lo com informações desnecessárias. Cada tela tem um objetivo primário bem definido, e elementos secundários são organizados de forma a não competir pela atenção.

**Consistência** é mantida através do uso de componentes, cores, tipografia e espaçamentos padronizados em toda a aplicação. Isso cria uma experiência coesa e previsível, reduzindo a carga cognitiva do usuário.

**Feedback Imediato** é fornecido para todas as ações do usuário através de animações sutis, notificações toast, mudanças de estado e indicadores de loading. O usuário nunca fica em dúvida se sua ação foi registrada.

**Eficiência** é priorizada através da otimização dos fluxos de trabalho, minimizando o número de cliques e o esforço cognitivo necessário para completar tarefas-chave. Atalhos de teclado e ações em lote são oferecidos para usuários avançados.

**Design Orientado a Dados** garante que as informações mais importantes sejam destacadas visualmente, utilizando gráficos, visualizações e hierarquia tipográfica para tornar dados complexos fáceis de entender rapidamente.

## 3.2. Sistema de Cores

| Cor | Código Hex | Uso |
| :--- | :--- | :--- |
| **Primária** | #6366F1 (Indigo) | CTAs, links, elementos ativos, sidebar ativa |
| **Secundária** | #8B5CF6 (Purple) | Badges premium, destaques especiais, gradientes |
| **Sucesso** | #10B981 (Green) | Confirmações, métricas positivas, crescimento |
| **Atenção** | #F59E0B (Amber) | Alertas, limites próximos, avisos |
| **Erro** | #EF4444 (Red) | Erros, ações destrutivas, problemas |
| **Neutro** | #64748B (Slate) | Textos secundários, bordas, backgrounds |

## 3.3. Tipografia

A tipografia utiliza a família **Inter** ou **Poppins** para headings (em negrito) e **Inter** ou **Open Sans** para o corpo do texto (regular). Para elementos que exibem códigos ou IDs, a fonte monospace **JetBrains Mono** é utilizada. Os tamanhos variam de 12px (captions) a 32px (headings principais), com line-height de 1.5 para legibilidade.

## 3.4. Espaçamento

O sistema de espaçamento é baseado em múltiplos de 8px, garantindo consistência e alinhamento perfeito em todos os elementos. Os tamanhos incluem: Base (8px), Pequeno (16px), Médio (24px), Grande (32px) e Extra Grande (48px).

## 3.5. Componentes Reutilizáveis

| Componente | Descrição | Comportamento |
| :--- | :--- | :--- |
| **Card de Análise** | Exibe informações resumidas de um vídeo analisado. | Hover destaca o card. Clique em ações específicas (ver detalhes, gerar roteiro). |
| **Badge de Plano** | Indica o plano do usuário ou funcionalidades premium. | Cores diferenciadas por plano. Usado em menu e modais de upgrade. |
| **Modal de Upgrade** | Apresenta opções de upgrade quando o usuário atinge um limite. | Comparação visual de planos. CTA destacado. Fechável com ESC ou clique fora. |
| **Empty State** | Exibido em seções sem conteúdo. | Ilustração amigável, mensagem explicativa e CTA para ação. |
| **Skeleton Loader** | Layout "fantasma" mostrado durante carregamento. | Melhora percepção de velocidade. Substitui spinners genéricos. |
| **Toast Notification** | Feedback não-bloqueante para ações. | Aparece no canto superior direito. Desaparece automaticamente. Cores por tipo (sucesso, erro, info). |

---

# 4. Diagramas de Fluxo de Navegação

## 4.1. Fluxo de Navegação Principal

O diagrama abaixo ilustra o fluxo completo de navegação da aplicação, desde o acesso inicial até as principais funcionalidades.

![Fluxo de Navegação Principal](/home/ubuntu/navigation_flow.png)

O usuário inicia acessando a aplicação. Se não estiver autenticado, é direcionado para a Landing Page, de onde pode ir para Login ou Cadastro. Após o cadastro, passa pelo Onboarding de 3 passos. Usuários autenticados acessam diretamente o Dashboard, que serve como hub central para todas as funcionalidades: Nova Análise, Minhas Análises, Meus Roteiros, Concorrentes, Alertas e Configurações.

A partir do Dashboard, o usuário pode iniciar uma Nova Análise, que passa por Configuração, Processamento e Resultados. Os Resultados permitem ações como Ver Detalhes, Gerar Roteiro, Salvar ou Exportar. A Geração de Roteiro segue seu próprio fluxo (Configuração → IA Gerando → Roteiro Gerado → Editar/Copiar/Salvar).

As Configurações incluem Perfil, Plano e Faturamento, e Notificações. O fluxo de Upgrade leva o usuário para uma Página de Checkout, e após o pagamento bem-sucedido, retorna ao Dashboard com o novo plano ativo.

## 4.2. Fluxo de Onboarding

O diagrama de onboarding detalha o processo de ativação de novos usuários.

![Fluxo de Onboarding](/home/ubuntu/onboarding_flow.png)

O novo usuário é recebido com uma Tela de Boas-Vindas que explica brevemente a plataforma. No Passo 1, ele seleciona seu nicho principal (Tech, Beleza, Fitness, Gaming ou Outro). No Passo 2, escolhe as plataformas de interesse (TikTok, YouTube ou Ambas). No Passo 3, decide se deseja fazer um Tour Guiado da interface.

Se optar pelo tour, o usuário é guiado por três telas principais (Dashboard, Nova Análise, Resultados) antes de completar o onboarding. Se pular o tour, vai direto para a conclusão. Ao finalizar, o sistema sugere uma Primeira Análise baseada no nicho selecionado, permitindo que o usuário experimente o valor da plataforma imediatamente antes de chegar ao Dashboard.

---

# 5. Boas Práticas de UX/UI Implementadas

## 5.1. Onboarding Progressivo

O onboarding foi projetado para ser rápido (menos de 2 minutos) e focado em coletar apenas as informações essenciais. O tour guiado é opcional, respeitando usuários que preferem explorar por conta própria. A sugestão de primeira análise baseada no nicho selecionado demonstra valor imediatamente, aumentando a taxa de ativação.

## 5.2. Hierarquia Visual Clara

Cada tela tem um objetivo primário claramente definido, com CTAs primários destacados em cor e tamanho. Informações secundárias são organizadas em cards e seções bem delimitadas. O uso de espaçamento generoso evita sobrecarga visual e melhora a legibilidade.

## 5.3. Feedback e Estados

Todos os estados possíveis da aplicação são considerados: loading (skeleton screens e spinners), sucesso (notificações e animações), erro (mensagens claras com ações de recuperação) e vazio (empty states com ilustrações e CTAs). Isso garante que o usuário nunca fique perdido ou sem saber o que fazer.

## 5.4. Acessibilidade

Embora não detalhado neste documento, a implementação deve seguir as diretrizes WCAG 2.1 AA, incluindo contraste adequado de cores, navegação por teclado, labels em formulários e textos alternativos em imagens.

## 5.5. Responsividade

A interface deve ser totalmente responsiva, adaptando-se a diferentes tamanhos de tela. A sidebar colapsa em mobile, cards são reorganizados em coluna única, e tabelas complexas podem ser substituídas por listas em dispositivos menores.

---

# 6. Próximos Passos para Implementação

## 6.1. Design de Alta Fidelidade

Com os wireframes e especificações definidos, o próximo passo é criar protótipos de alta fidelidade no Figma, incluindo todas as telas, componentes e estados. Isso permitirá testes de usabilidade antes do desenvolvimento.

## 6.2. Sistema de Design (Design System)

Documentar todos os componentes, cores, tipografia e padrões em um Design System centralizado (ex: Storybook) facilitará a manutenção e garantirá consistência durante o desenvolvimento e evolução do produto.

## 6.3. Testes de Usabilidade

Realizar testes com usuários reais (representando as três personas) para validar os fluxos, identificar pontos de fricção e iterar antes do lançamento. Testes A/B podem ser usados para otimizar CTAs e conversões.

## 6.4. Implementação Iterativa

Seguir uma abordagem ágil, implementando as telas em sprints e validando com usuários beta. Começar pelo fluxo principal (Dashboard → Nova Análise → Resultados) e expandir para funcionalidades secundárias.

