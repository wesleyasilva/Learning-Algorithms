from Dijkstra import Dijkstra as D
import networkx as nx

grafo1 = {'a':{'b':10, 'd':9, 'c':3},
         'b':{'a':10,'c':2},
         'c':{'b':2, 'a':3, 'd':4},
         'd':{'a':9, 'c':4}}

graph1 = D(grafo1)
print(graph1.dijkstra('a', 'd'))