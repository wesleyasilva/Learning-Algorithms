import numpy as np

class Dijkstra(object):
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, u, v):
        menor_distancia = {}
        pred = {}
        G = self.graph
        caminho = []
        
        for vertice in G:
            menor_distancia[vertice] = np.inf
        menor_distancia[u] = 0

        while G:
            minVert = None
            for vertice in G:
                if minVert is None:
                    minVert = vertice
                elif menor_distancia[vertice] < menor_distancia[minVert]:
                    minVert = vertice
            
            for vert, custo in self.graph[minVert].items():
                if custo + menor_distancia[minVert] < menor_distancia[vert]:
                    menor_distancia[vert] = custo + menor_distancia[minVert]
                    pred[vert] = minVert
            G.pop(minVert)
        
        vertice_atual = v
        
        while vertice_atual != u:
            caminho.insert(0,vertice_atual)
            vertice_atual = pred[vertice_atual]
        
        caminho.insert(0,u)
        if menor_distancia[v] != np.inf:
           return str(caminho)