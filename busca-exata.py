import time
from random import randint


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
            'citations-given': [],  # Citações feitas
            'cited-by': [],  # Citações recebidas
            'power': 0, # Índice de influência
        }
        nodes[v[0]] = node
    vertices.close()

    # Arestas
    edges = open(edgesFile, 'r', encoding='utf8')
    next(edges)
    for edge in edges:
        e = edge.split('\t')
        citation = {
            'from': e[0],  # Artigo citador
            'to': e[1].split()[0],  # Artigo citado
            'weight': int(e[1].split()[1]),  # Peso da aresta, padrão 1
        }
        nodes[e[0]]['citations-given'].append(citation)  # Adiciono quem eu cito
        nodes[e[1].split()[0]]['cited-by'].append(citation)  # Adiciono uma citação pro citado
    edges.close()

    return nodes


# Heurística
def calcInfluencePower(nodes, node, year, ignoreFuture=False):
    # Pesos
    CURRENT_YEAR_CITATIONS = 3 # Citações recebidas no ano corrente
    LAST_YEAR_CITATIONS = 2 # Citações recebidas no ano passado
    PAST_CITATIONS = 1 # Citações recebidas de anos anteriores
    FUTURE_CITATIONS = 0 if ignoreFuture else 1 # Citações recebidas de anos futuros
    CITATIONS_GIVEN = 1/2 # Citações feitas

    nodeYear = int(nodes[node]['year']) if nodes[node]['year'] else None

    # Calcula parte do índice de influência do nó baseado nos anos das citações recebidas
    power = 0
    if nodeYear:
        for citedBy in nodes[node]['cited-by']:
            citedByYear = int(nodes[citedBy['to']]['year']) if nodes[citedBy['to']]['year'] else None
            if citedByYear and citedByYear == nodeYear:
                power += CURRENT_YEAR_CITATIONS
            elif citedByYear and citedByYear == nodeYear - 1:
                power += LAST_YEAR_CITATIONS
            elif citedByYear and citedByYear < nodeYear - 1:
                power += PAST_CITATIONS
            elif citedByYear:
                power += FUTURE_CITATIONS

    # Calcula parte do índice de influência do nó baseado nas citações feitas
    power += len(nodes[node]['citations-given']) * CITATIONS_GIVEN

    return power


def searchTopInfluencers(nodes, year, top=10, rootNode=None, ignoreFuture=False):
    # Atribui o índice de influência para os nós
    for node in nodes:
        nodes[node]['power'] = calcInfluencePower(nodes, node, year, ignoreFuture)

    root = randint(0, len(nodes.items())) if not rootNode else rootNode # Atribui um nó aleatório ou o nó passado via parâmetro
    rank = []
    frontier = []
    explored = []

    frontier.append(root) # Adiciona a raíz como primeiro nó da fronteira
    while len(frontier):
        node = frontier.pop(0) # FIFO

        if not node in explored:
            explored.append(node)
            if len(rank) < top:
                rank.append({'id': str(node), 'power': nodes[str(node)]['power']})
            else:
                # Encontra o top menos influente no rank
                ranked2 = [t['power'] for t in rank]
                leastInfluencer = min(ranked2)
                index = ranked2.index(min(ranked2))

                # Substitui o nó caso seja mais influente que algum no rank
                if nodes[node]['power'] > leastInfluencer:
                    rank[index] = {'id': str(node), 'power': nodes[str(node)]['power']}

            # Adiciona as citações feitas à fronteira
            for citationGiven in nodes[str(node)]['citations-given']:
                if not citationGiven['to'] in explored:
                    frontier.append(citationGiven['to'])

            # Adiciona as citações recebidas à fronteira
            for citedBy in nodes[str(node)]['cited-by']:
                if not citedBy['from'] in explored:
                    frontier.append(citedBy['from'])

    return {'rank': rank, 'root': root}


def searchTopInfluencersReachness(tops, nodes, isTopsWithin=False):
    frontier = [t['id'] for t in tops['rank']] # Copia os tops sem bagunçar as referências
    explored = []

    while len(frontier):
        node = frontier.pop(0) # FIFO
        if not node in explored:
            explored.append(node)
            for citation in nodes[node]['citations-given']:
                if not citation['to'] in explored:
                    frontier.append(citation['to'])

    # Remove os tops do vetor de alcançados
    if not isTopsWithin:
        for top in [t['id'] for t in tops['rank']]:
             if top in explored:
                 explored.remove(top)

    return {
        'Raíz': tops['root'],
        'Total:': str(len(explored)) + ' nós',
        'Mais Influentes:': sorted(tops['rank'], key=lambda k: k['power'], reverse=True),
        'Alcançados:': sorted([{'id': r, 'power': nodes[r]['power']} for r in explored], key=lambda e: e['power'], reverse=True)
    }


# Main
tempoInicial = time.clock()

YEAR = 2000 # Ano utilizado pela busca
nodes = buildNodes('vertices.txt', 'edges.txt') # Cria estrutura de dados

for i in range(5): # Executa a busca algumas vezes para o caso de cair em bolhas sociais
    print('\n')
    topInfluencers = searchTopInfluencers(nodes, YEAR) # Realiza a busca com heurística passando um ano como parâmetro
    reachness = searchTopInfluencersReachness(topInfluencers, nodes) # Descobre o alcance dos mais influentes
    for key, value in reachness.items(): # Imprime os resultados
        print(key, value)

print('\nTempo de execução: ' + str(round(time.clock() - tempoInicial, 2)) + 's')
