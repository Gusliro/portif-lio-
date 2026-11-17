# Gustavo Trimpler Reinhold | Portfólio

Estudo Tecnologia em Sistemas para Internet na UFSM. Desenvolvo agentes em Python, automações de processos, aplicações web e protótipos em realidade virtual.

[IA e automação](#ia-e-automação) · [Front-end](#front-end) · [Back-end](#back-end) · [Design de interfaces](#design-de-interfaces) · [Realidade virtual](#realidade-virtual)

## IA e automação

### Agente de recomendação de conteúdo

Em um trabalho da UFSM, implementei um agente em Python que acompanha visualizações, cliques e tempo de permanência. Ele atualiza a pontuação de interesse por categoria a cada interação e sugere itens inéditos para cada perfil. As regras são explícitas e podem ser acompanhadas no terminal.

[Executar a demonstração em Python](projetos/recomendador/README.md) · [Ler o código](projetos/recomendador/agente_recomendacao.py)

### Preparador de planilhas fiscais

Desenvolvi uma ferramenta em **Excel e VBA** que transforma arquivos CSV em cinco abas de um modelo de planejamento fiscal. Ela identifica as colunas pelo cabeçalho, aplica regras configuráveis e encaminha registros que exigem revisão para uma aba de pendências. Usei o **Codex** para preparar dados fictícios para testar importações e cenários de erro.

[Ver o fluxo e os critérios de conferência](projetos/automacao-fiscal.md)

### Agente de eficiência energética residencial

Em um projeto acadêmico, implementei em **Python** um agente que prioriza sugestões de economia de energia conforme os dados dos equipamentos e as preferências do usuário. A simulação ajusta a ordem das sugestões com base nas respostas recebidas.

### Outras automações

- **Envio de NFS-e.** Durante o estágio na Migrate Brasil, desenvolvi uma automação em Python e PyAutoGUI para o fluxo de envio de notas fiscais de serviço.
- **Farm de moedas no Club Penguin Journey.** Protótipo em Python com Selenium e PyAutoGUI para automatizar a mineração de moedas no Firefox. O modo PyAutoGUI permite calibrar os pontos de interação na tela e verifica o foco da janela durante a execução.
- **Análise esportiva.** Protótipo local em Python que usa um modelo de Poisson para estimar probabilidades a partir de dados de exemplo e gerar relatórios.

## Front-end

| Projeto | Interface |
| --- | --- |
| **[Latitude 180](projetos/latitude-180.md)** | Repaginação do site da agência em React e Vite, com navegação responsiva, roteiros e formulário de contato por e-mail ou WhatsApp. A repaginação foi descontinuada por decisão do cliente. |
| **[Biblioteca Virtual](projetos/biblioteca-virtual.md)** | Interface em JSP com estantes para livros lidos e em leitura, busca por título ou autor e painel com estatísticas da coleção. |
| **Controle de Gastos** | Aplicação acadêmica em PHP com telas de login, formulário de despesas e painel financeiro. |
| **Trabalhos de Programação Web** | Portfólio acadêmico com área de login. Outros exercícios incluem cadastro de usuários e CRUD de produtos em PHP. |

## Back-end

| Projeto | Implementação |
| --- | --- |
| **[Biblioteca Virtual](projetos/biblioteca-virtual.md)** | Aplicação full stack em Java 21 e Spring Boot 3.5, com login por sessão e operações em PostgreSQL via JDBC. O catálogo e os indicadores de leitura são consultados por usuário. |
| **Avaliador de Projetos** | API REST em Spring Boot com recursos para alunos, projetos e avaliações, validação, tratamento de erros e migrações Flyway. |

## Design de interfaces

### Biblioteca Virtual

O painel organiza a coleção em duas estantes e mostra o total de livros, o progresso das leituras e a média das notas. A interface cria uma capa com título e autor quando o livro não tem imagem cadastrada.

[Ver a estante com as capas e ler o estudo de caso](projetos/biblioteca-virtual.md)

## Realidade virtual

### Torno mecânico CDL-400

Projeto acadêmico do **CTISM/UFSM** para explorar o uso da realidade virtual no ensino de segurança industrial. Minha contribuição envolve modelagem de componentes no Blender, integração à Unity e testes no Meta Quest 2.

[Acompanhar o desenvolvimento do torno](projetos/torno-mecanico-rv.md)

## Projetos complementares

- **Síntese de sons de chuva.** Gerador em Python com perfis configuráveis, duração parametrizada e reprodução por semente.

[Perfil no GitHub](https://github.com/Gusliro)
