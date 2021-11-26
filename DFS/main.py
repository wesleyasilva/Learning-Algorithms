from DFS import Dfs as Dfs

grafo = {'a':set(['b','c','d']),
         'b':set(['a']),
         'c':set(['a']),
         'd':set(['a','e']),
         'e':set(['d','f']),
         'f':set(['e'])}

G = Dfs()
print('\tDFS(a,f): '+str(list(G.caminho_dfs(grafo, 'a', 'f')))+'\n')
