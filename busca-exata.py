import time

def buildNodes(verticesFile, edgesFile):
    nodes = {}

    # Vértices
    vertices = open(verticesFile, encoding='utf8')
    next(vertices) # Pula a primeira linha do arquivo
    for vertex in vertices:
        v = vertex.split('\t')
        node = {
            'id': int(v[0]),
            'title': v[1],
            'year': v[2] or None,
            'venue': v[3] or None, # Editor
            'authors': v[4][:-1].split(',') if len(v[4][:-1].split(',')) > 1 else [], # Remove '\n' e cria vetor de autores
            'citations': [] # Edges
        }
        nodes[v[0]] = node
    vertices.close()

    # Arestas
    edges = open(edgesFile, encoding='utf8')
    next(edges)
    for edge in edges:
        e = edge.split('\t')
        citation = {
            'from': e[0],  # Documento citador
            'to': e[1].split()[0],  # Documento citado
            'weight': int(e[1].split()[1]),  # Peso da aresta, padrão 1
        }
        nodes[e[0]]['citations'].append(citation)
    edges.close()

    return nodes


def buildGraph(nodes):
    graph = {}

    # TODO Continuar

    return graph


def searchTopInfluencers(graph, top = 10):
    rank = []

    # TODO Continuar

    return rank

# Main
tempoInicial = time.clock()

nodes = buildNodes('vertices.txt', 'edges.txt')
graph = buildGraph(nodes)
searchTopInfluencers(graph)

print('\nTempo de execução: ' + str(round(time.clock() - tempoInicial,2)) + 's')