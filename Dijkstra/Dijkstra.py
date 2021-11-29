import numpy as np

class Dijkstra(object):
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, u, v):
        shortest_distance = {}
        pred = {}
        G = self.graph
        way = []
        
        for vertex in G:
            shortest_distance[vertex] = np.inf
        shortest_distance[u] = 0

        while G:
            minVert = None
            for vertex in G:
                if minVert is None:
                    minVert = vertex
                elif shortest_distance[vertex] < shortest_distance[minVert]:
                    minVert = vertex
            
            for vert, cost in self.graph[minVert].items():
                if cost + shortest_distance[minVert] < shortest_distance[vert]:
                    shortest_distance[vert] = cost + shortest_distance[minVert]
                    pred[vert] = minVert
            G.pop(minVert)
        
        current_vertex = v
        
        while current_vertex != u:
            way.insert(0,current_vertex)
            current_vertex = pred[current_vertex]
        
        way.insert(0,u)
        if shortest_distance[v] != np.inf:
           return str(way)
