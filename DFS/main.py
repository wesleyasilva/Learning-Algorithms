from DFS import Dfs as Dfs

graph = {'a':set(['b','c','d']),
         'b':set(['a']),
         'c':set(['a']),
         'd':set(['a','e']),
         'e':set(['d','f']),
         'f':set(['e'])}

G = Dfs()
print('\tDFS(a,f): '+str(list(G.dfs_path(graph, 'a', 'f')))+'\n')
