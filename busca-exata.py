import time


def buildNodes(verticesFile, edgesFile):
    nodes = {}

    # Vértices
    vertices = open(verticesFile, 'r', encoding='utf8')
    next(vertices)  # Pula a primeira linha do arquivo
    for vertex in vertices:
        v = vertex.split('\t')
        node = {
            'id': int(v[0]),
            'title': v[1],
            'year': v[2] or None,
            'venue': v[3] or None,  # Editor
            'authors': v[4][:-1].split(',') if len(v[4][:-1].split(',')) > 1 else [], # Remove '\n' e cria vetor de autores
            'feitos': [],  # Edges
            'recebidos': [],  # Edges
            'peso': 0,  # TODO trocar por formula da heuristica
            'estado': 0  # Estado do nó, meta, inicio...
        }
        nodes[v[0]] = node
    vertices.close()

    # Arestas
    edges = open(edgesFile, 'r', encoding='utf8')
    next(edges)
    for edge in edges:
        e = edge.split('\t')
        citation = {
            'from': e[0],  # Documento citador
            'to': e[1].split()[0],  # Documento citado
            'weight': int(e[1].split()[1]),  # Peso da aresta, padrão 1
        }
        nodes[e[0]]['feitos'].append(citation)  # Adiciono quem eu cito
        nodes[e[1].split()[0]]['recebidos'].append(citation)  # adiciono uma citação pro citado
        nodes[e[1].split()[0]]['peso'] += 1  # TODO trocar por formula da heuristica
    edges.close()

    return nodes


def buildGraph(nodes):
    graph = {}

    # TODO Continuar

    return graph


def searchTopInfluencers(graph, top=10):
    rank = []

    # TODO Continuar

    return rank


def expandirNo(node):
    return node['recebidos']


def escolheNoFolha(nodes):
    escolhido = {}

    for node in nodes:
        escolhido = nodes[node]

    return escolhido


def isElementoInArray(elemento, array):
    retorno = 0

    for el in array:
        if el == elemento:
            retorno = 1

    return retorno


def funcaoBuscaGrafo(noInicial):
    # inicializar frontier usando o estado inicial do problema
    frontier = []
    frontier.append(noInicial)

    conjuntoExplorado = []

    retorno = 'sucesso'

    while True:
        if len(frontier) == 0:
            retorno = 'falha'
            break

        noFolhaAtual = escolheNoFolha(frontier)
        frontier.remove(noFolhaAtual)

        if noFolhaAtual['estado'] == 1:  # Nó está no estado meta
            # retorna solucao
            break

        conjuntoExplorado.append(noFolhaAtual)

        filhos = expandirNo(noFolhaAtual)

        # Adiciona filhos que nao estão no conjunto explorado ou na fronteira
        for filho in filhos:
            if isElementoInArray(filhos[filho], conjuntoExplorado) == 0 or isElementoInArray(filhos[filho],
                                                                                             frontier) == 0:
                frontier.append(filhos[filho])

    return retorno


def searchTopInfluencersReachness(tops, nodes, isTopsWithin=False):
    frontier = tops[:] # Copia os tops sem bagunçar as referências
    explored = []

    while len(frontier):
        node = frontier.pop(0) # FIFO
        if not node in explored:
            explored.append(node)
            for citation in nodes[node]['feitos']:
                if not citation['to'] in explored:
                    frontier.append(citation['to'])

    # Remove os tops do array de alcançados
    if not isTopsWithin:
        for top in tops:
            explored.remove(top)

    return {'total': len(explored), 'tops': tops, 'reached': explored}


# Main
tempoInicial = time.clock()

nodes = buildNodes('vertices.txt', 'edges.txt')

topInfluencers = ['354', '411', '2002'] # TODO substituir pelo retorno da busca com heurísitica
reachness = searchTopInfluencersReachness(topInfluencers, nodes, True)
for key, value in reachness.items(): # Imprime os resultados
    print(key, value)

print('\nTempo de execução: ' + str(round(time.clock() - tempoInicial, 2)) + 's')
