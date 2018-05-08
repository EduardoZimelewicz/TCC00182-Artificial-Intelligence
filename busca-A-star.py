import time
from random import randint

def buildNodes(verticesFile, edgesFile):
    nodes = {}

    # Vértices
    vertices = open(verticesFile, 'r', encoding='utf8')
    next(vertices) # Pula a primeira linha do arquivo
    for vertex in vertices:
        v = vertex.split('\t')
        node = {
            'id': int(v[0]),
            'title': v[1],
            'year': v[2] or None,
            'venue': v[3] or None, # Editor
            'authors': v[4][:-1].split(',') if len(v[4][:-1].split(',')) > 1 else [], # Remove '\n' e cria vetor de autores
            'feitos': [], # Edges
            'recebidos': [], # Edges
            'peso': 0, # TODO trocar por formula da heuristica 'h'
            'funcao': 0, # f = g + h
            'g': 0,
            'estado': 0 #Estado do nó, meta, inicio...
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
        nodes[e[0]]['feitos'].append(citation) # Adiciono quem eu cito
        nodes[e[1].split()[0]]['recebidos'].append(citation) # adiciono uma citação pro citado
        nodes[e[1].split()[0]]['peso'] += 1 # TODO trocar por formula da heuristica
    edges.close()

    return nodes


def buildGraph(nodes):
    graph = {}

    # TODO Continuar

    return graph

def acharNoPorId(nodes, id):
    retorno = {}

    for node in nodes:
        if node == id:
            retorno = nodes[node]

    return retorno

def acharNoPorIdFronteira(frontier, id):
    retorno = {}

    for node in frontier:
        if node['id'] == int(id):
            retorno = node

    return retorno

def searchTopInfluencers(graph, top = 10):
    rank = []

    # TODO Continuar

    return rank

def acharNosNaoCitados(nodes):
    nodesSaida = []

    for node in nodes:
        if len(nodes[node]['recebidos']) == 0:
            nodesSaida.append(nodes[node])

    return nodesSaida

def definirNoSaidaAleatorio(nodes):
    nodesSaida = acharNosNaoCitados(nodes)

    quantidade = len(nodesSaida)
    nodeSaida = {}
    posicaoNode = randint(0,quantidade-1)
    contador = 0

    for node in nodesSaida:
        if contador == posicaoNode:
            nodeSaida = node
        contador = contador + 1

    for n in nodes:
        if nodes[n] == nodeSaida:
            nodes[n]['estado'] = 1

def definirNoEntrada(nodes):
    retorno = {}

    indexNo = randint(0, 1000)

    for node in nodes:
        if nodes[node]['id'] == indexNo:
            retorno = nodes[node]

    return retorno

def expandirNo(node):
    return node['filhos']

def escolheNoFolha(nodes):
    escolhido = {}

    for node in nodes:
        escolhido = node
        break

    return escolhido

def replaceElementoInArray(elementoOld, elementoNew, array):
    for el in array:
        if el == elementoOld:
            el = elementoNew

def isElementoInArray(elemento, array):
    retorno = 0

    for el in array:
        if el['id'] == int(elemento['from']):
            retorno = 1

    return retorno


def funcaoBuscaGrafo(noInicial, nodes):
    #   no = {
    #       'state': 0,
    #       'parent': {},
    #       'action': 0,
    #       'pathCost': 0
    #       'filhos': noInicial['recebidos'],  # Edges dos filhos
    #       'g': 0,
    #       'id': noInicial['id']
    #   }

    #inicializar frontier usando o estado inicial do problema
    frontier = []

    no = {
        'state': 0, #Estado inicial
        'parent': {},
        'action': 0,
        'pathCost': noInicial['peso'],
        'filhos': noInicial['recebidos'], #Edges dos filhos
        'g': 0,
        'id': noInicial['id']
    }
    frontier.append(no)

    conjuntoExplorado = []

    retorno = []

    while True:
        if len(frontier) == 0:
            retorno = conjuntoExplorado
            break

        noFolhaAtual = escolheNoFolha(frontier)
        frontier.remove(noFolhaAtual)

        conjuntoExplorado.append(noFolhaAtual)


        filhos = expandirNo(noFolhaAtual)

        #Adiciona filhos que nao estão no conjunto explorado ou na fronteira
        for filho in filhos:
            if isElementoInArray(filho,conjuntoExplorado) == 0 and isElementoInArray(filho,frontier) == 0:
                #Cria no do filho que será incluido na fronteira
                filhoEmNodes = acharNoPorId(nodes, filho['from'])
                noCandidato = {
                    'state': acharNoPorId(nodes,filho['from'])['estado'],
                    'parent': noFolhaAtual,
                    'action': 0,
                    'pathCost': acharNoPorId(nodes,filho['from'])['peso'] + noFolhaAtual['g'],  # f = h + g
                    'filhos': acharNoPorId(nodes,filho['from'])['recebidos'],
                    'g': noFolhaAtual['g'],
                    'id': acharNoPorId(nodes,filho['from'])['id']
                }
                frontier.append(noCandidato)
            else:
                if isElementoInArray(filho,frontier) == 1: # Elemento na fronteira?
                    gg = acharNoPorId(nodes,filho['from'])
                    if noFolhaAtual['g'] + 1 > acharNoPorIdFronteira(frontier,filho['from'])['g']: # Se seu pathCost é menor que no caminho atual
                        noCandidato = {
                            'state': acharNoPorId(nodes,filho['from'])['estado'],
                            'parent': noFolhaAtual,
                            'action': 0,
                            'pathCost': acharNoPorId(nodes,filho['from'])['peso'] + noFolhaAtual['g'],  # f = h + g
                            'filhos': acharNoPorId(nodes,filho['from'])['recebidos'],
                            'g': noFolhaAtual['g'],
                            'id': acharNoPorId(nodes,filho['from'])['id']
                        }
                        replaceElementoInArray(filho,noCandidato,frontier)

    influencias = []

    for r in retorno:
        info = [r['id'],r['pathCost']]

        influencias.append(info)

    influencias.sort(key=getKey)

    print('INFLUÊNCIAS\n\n')

    for i in reversed(influencias):
        print('id: ' + str(i[0]) + '   influencia: ' + str(i[1]) + '\n')

    return retorno

def getKey(item):
    return item[1]

def printaVisitados(visitados):
    #   no = {
    #       'state': 0,
    #       'parent': {},
    #       'action': 0,
    #       'pathCost': 0
    #       'filhos': noInicial['recebidos'],  # Edges dos filhos
    #       'g': 0,
    #       'id': noInicial['id']
    #   }

    for v in visitados:
        if v['parent'] != {}:
            pai = str(v['parent']['id'])
        else:
            pai = ''
        print('No ' + str(v['id']) + '\nEstado: ' + str(v['state']) + '\nPai: ' + pai + '\nInfluencia: ' + str(v['pathCost']) + '\nFilhos:\n')
        for f in v['filhos']:
            print('    No ' + f['from'] + '\n')

def influentes(visitados):
    counter = 0

    for v in visitados:
        print(str(v['pathCost']) + '\n')
        counter = counter + 1
        if counter > 10:
            break

# Main
tempoInicial = time.clock()

nodes = buildNodes('vertices.txt', 'edges.txt')

for i in range(5):
    nodeEntrada = definirNoEntrada(nodes)

    printaVisitados(funcaoBuscaGrafo(nodeEntrada, nodes))

    #print(nodes)
graph = buildGraph(nodes)
searchTopInfluencers(graph)

print('\nTempo de execução: ' + str(round(time.clock() - tempoInicial,2)) + 's')