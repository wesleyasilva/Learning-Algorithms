grafo = {'a': set(['b', 'c']),
         'b': set(['a', 'x']),
         'c': set(['a', 'h', 'x', 'y']),
         'f': set(['l']),
         'h': set(['c', 'm', 'n']),
         'l': set(['f', 'x']),
         'm': set(['h']),
         'n': set(['h', 'r']),
         'p': set(['r', 'x', 'y']),
         'r': set(['n', 'p', 'v', 'z']),
         'v': set(['r', 'y']),
         'x': set(['b', 'c', 'l', 'p']),
         'z': set(['r']),
         'y': set(['c', 'p', 'v'])}

def bfs(graph, s):
    visitado,fila = set(),[s]
    while fila:
       vertice = fila.pop(0)
       if vertice not in visitado:
           visitado.add(vertice)
           fila.extend(graph[vertice]-visitado)
    return visitado

def caminho_bfs(graph, s, t):
    fila = [(s, [s])]
    while fila:
        (vertice, caminho) = fila.pop(0)
        for proximo in graph[vertice] - set(caminho):
            if proximo == t:
                yield caminho + [proximo]
            else:
                fila.append((proximo, caminho + [proximo]))

def menor_caminho(graph, s, t):
    try:
        return caminho_bfs(graph, s, t)
    except StopIteration:
        return None

print('Vértices Visitados: ',bfs(grafo, 'a'),'\n')

print(menor_caminho(grafo, 'a', 'y'))

c = 1
for caminho in caminho_bfs(grafo, 'a', 'z'):
    print('%dº Caminho Possível' % c)
    print(caminho,'\n')
    c+=1