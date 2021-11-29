from Dijkstra import Dijkstra as D

graph = {'a':{'b':10, 'd':9, 'c':3, 'e':3},
         'b':{'a':10,'c':2},
         'c':{'b':2, 'a':3, 'd':4, 'e':5},
         'd':{'a':9, 'c':4, 'e':2},
         'e':{'a':3,'c':5,'d':2}}

graph_object = D(graph)
print(graph_object.dijkstra('a', 'd'))
