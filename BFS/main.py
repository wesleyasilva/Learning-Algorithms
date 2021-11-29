from BFS import Bfs as Bfs

graph = {'a': set(['b', 'c']),
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
print('Visited vertices: ',G.bfs(graph, 'a'),'\n')
print('Best Way/Path: ',list(G.shortest_path(graph,'a','y')))

c = 1
for way in G.bfs_path(graph, 'a', 'z'):
    print('%dº Possible Path' % c)
    print(way,'\n')
    c+=1
