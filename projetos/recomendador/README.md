# Agente de recomendação de conteúdo

Implementação acadêmica em Python com uma amostra fictícia. O agente mantém um estado por perfil e recomenda conteúdos com base na pontuação acumulada por categoria. Visualizações, tempo de permanência e reações a recomendações alteram essa pontuação.

## Executar

Na raiz do portfólio, entre nesta pasta e execute o script com Python 3. A demonstração usa a biblioteca padrão.

```sh
cd projetos/recomendador
python -X utf8 agente_recomendacao.py
```

O perfil fictício recebe primeiro uma sugestão sobre dados. Depois de interagir com conteúdo de XR, a categoria sobe na pontuação e a sugestão seguinte muda. O terminal mostra as preferências e a decisão após cada evento.

O CTR histórico exibido no final é calculado como cliques divididos pela soma de cliques e recomendações ignoradas no CSV. A amostra serve para reproduzir o comportamento das regras. Uma comparação futura de qualidade pode usar eventos reservados e uma linha de base, como recomendar por popularidade.

[Voltar ao portfólio](../../README.md)
