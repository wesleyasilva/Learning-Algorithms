from BFS import Bfs as Bfs

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

G =  Bfs()
print('Vértices Visitados: '+str(G.bfs(grafo, 'a'))+'\n')
print('Melhor Caminho: ',list(G.menor_caminho(grafo,'a','y')))

