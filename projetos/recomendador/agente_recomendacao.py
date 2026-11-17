"""Trabalho 1 - Agente de recomendacao de conteudo."""

import csv


ARQUIVO_CONTEUDOS = "conteudos.csv"
ARQUIVO_HISTORICO = "historico.csv"


def carregar_conteudos():
    """Le o CSV."""
    conteudos = []

    with open(ARQUIVO_CONTEUDOS, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            conteudos.append(linha)

    return conteudos


def carregar_historico():
    """Le o historico e coloca os eventos em ordem"""
    historico = []

    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            historico.append(linha)

    ordenar_historico(historico)
    return historico


def ordenar_historico(historico):
    """Organiza o historico pelo momento usando bubble sort basicao."""
    for indice_atual in range(len(historico)):
        for proximo_indice in range(len(historico) - 1):
            momento_atual = int(historico[proximo_indice]["momento"])
            proximo_momento = int(historico[proximo_indice + 1]["momento"])

            if momento_atual > proximo_momento:
                temporario = historico[proximo_indice]
                historico[proximo_indice] = historico[proximo_indice + 1]
                historico[proximo_indice + 1] = temporario


def buscar_conteudo(conteudos, identificador):
    for conteudo in conteudos:
        if conteudo["id"] == identificador:
            return conteudo
    return None


def criar_estado():
    """Cria o estado interno inicial de um usuario."""
    return {
        "preferencias": {},
        "visualizados": [],
        "recomendados": [],
        "recomendacoes_historicas": [],
    }


def alterar_preferencia(estado, categoria, pontos):
    """Soma ou reduz pontos de interesse por categoria."""
    if categoria not in estado["preferencias"]:
        estado["preferencias"][categoria] = 0

    estado["preferencias"][categoria] += pontos


def atualizar_estado(estado, evento, conteudos):
    """Transforma uma percepcao recebida em uma atualizacao do estado."""
    conteudo = buscar_conteudo(conteudos, evento["conteudo_id"])

    if conteudo is None:
        print("Conteudo nao encontrado: " + evento["conteudo_id"])
        return

    categoria = conteudo["categoria"]
    tipo_evento = evento["evento"]

    if tipo_evento == "visualizacao":
        if conteudo["id"] not in estado["visualizados"]:
            estado["visualizados"].append(conteudo["id"])

        alterar_preferencia(estado, categoria, 1)

        # Permanecer vira sinal de interesse.
        tempo = evento["tempo_segundos"]
        if tempo != "" and float(tempo) >= 120:
            alterar_preferencia(estado, categoria, 1)

    elif tipo_evento == "clique_recomendacao":
        alterar_preferencia(estado, categoria, 2)

    elif tipo_evento == "ignorou_recomendacao":
        alterar_preferencia(estado, categoria, -1)


def escolher_recomendacao(estado, conteudos):
    melhor_conteudo = None
    maior_pontuacao = -9999

    for conteudo in conteudos:
        ja_foi_usado = (
            conteudo["id"] in estado["visualizados"]
            or conteudo["id"] in estado["recomendados"]
            or conteudo["id"] in estado["recomendacoes_historicas"]
        )

        if not ja_foi_usado:
            categoria = conteudo["categoria"]
            pontuacao = estado["preferencias"].get(categoria, 0)

            if pontuacao > maior_pontuacao:
                maior_pontuacao = pontuacao
                melhor_conteudo = conteudo

    return melhor_conteudo


def mostrar_estado(estado):
    print("Preferencias por categoria:", estado["preferencias"])
    print("Conteudos visualizados:", estado["visualizados"])
    print("Conteudos recomendados pelo agente:", estado["recomendados"])


def mostrar_metricas(historico, estados):
    """Calcula medidas cheio de if e else para avaliar o comportamento do agente."""
    cliques = 0
    ignoradas = 0
    soma_tempos = 0
    quantidade_tempos = 0
    recomendacoes_geradas = 0

    for evento in historico:
        if evento["evento"] == "clique_recomendacao":
            cliques += 1
        elif evento["evento"] == "ignorou_recomendacao":
            ignoradas += 1
        elif evento["evento"] == "visualizacao":
            if evento["tempo_segundos"] != "":
                soma_tempos += float(evento["tempo_segundos"])
                quantidade_tempos += 1

    for usuario in estados:
        recomendacoes_geradas += len(estados[usuario]["recomendados"])

    total_feedbacks = cliques + ignoradas
    if total_feedbacks > 0:
        ctr = cliques / total_feedbacks * 100
        taxa_ignoradas = ignoradas / total_feedbacks * 100
    else:
        ctr = 0
        taxa_ignoradas = 0

    if quantidade_tempos > 0:
        tempo_medio = soma_tempos / quantidade_tempos
    else:
        tempo_medio = 0

    print("\n=== Medidas de desempenho ===")
    print("Recomendacoes geradas pelo agente:", recomendacoes_geradas)
    print("CTR historico: {:.1f}%".format(ctr))
    print("Taxa de recomendacoes ignoradas: {:.1f}%".format(taxa_ignoradas))
    print("Tempo medio de permanencia: {:.1f} segundos".format(tempo_medio))


def main():
    conteudos = carregar_conteudos()
    historico = carregar_historico()
    estados = {}

    print("=== Simulacao do agente de recomendacao ===")

    for evento in historico:
        usuario = evento["usuario"]

        if usuario not in estados:
            estados[usuario] = criar_estado()

        estado = estados[usuario]

        if evento["evento"] == "recomendacao":
            estado["recomendacoes_historicas"].append(evento["conteudo_id"])
            print("\nAcao historica: " + usuario + " recebeu o conteudo " + evento["conteudo_id"])
            continue

        print("\nPercepcao:", evento)
        atualizar_estado(estado, evento, conteudos)
        print("Estado interno depois da percepcao:")
        mostrar_estado(estado)

        # O agente recomenda um novo conteudo apenas depois de uma visualizacao.
        if evento["evento"] == "visualizacao":
            recomendacao = escolher_recomendacao(estado, conteudos)

            if recomendacao is None:
                print("Decisao: nao existe conteudo novo para recomendar.")
            else:
                estado["recomendados"].append(recomendacao["id"])
                print(
                    "Decisao e acao: recomendar "
                    + recomendacao["id"]
                    + " - "
                    + recomendacao["titulo"]
                    + " ("
                    + recomendacao["categoria"]
                    + ")."
                )
        else:
            print("Decisao: atualizar o estado e esperar nova visualizacao.")

    mostrar_metricas(historico, estados)


main()
