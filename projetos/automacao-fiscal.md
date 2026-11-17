# Automação de planilhas fiscais com Excel e VBA

## Problema

O planejamento fiscal recebe relatórios de origens diferentes. Cada rotina precisa identificar as colunas de entrada, aplicar regras próprias e produzir uma saída no formato do modelo, deixando visíveis os registros que exigem conferência.

## Implementação

Implementei as cinco rotinas em um arquivo Excel com macros. O importador localiza as colunas pelo nome do cabeçalho e as regras ficam em tabelas de parâmetros editáveis. A planilha encaminha os resultados para as abas correspondentes e registra o motivo quando uma linha precisa de revisão.

O fluxo vai da importação e do mapeamento de colunas à aplicação das regras, ao preenchimento das abas e à conferência de pendências.

## Testes e uso do Codex

Usei o Codex para preparar arquivos fictícios de teste de importação e de erro. A documentação da ferramenta registra uma conferência entre o total de linhas lidas e a soma de linhas exportadas, excluídas e rejeitadas. Essa reconciliação permite detectar quando um registro desaparece do fluxo.

[Voltar ao portfólio](../README.md)
