class Dfs(object):
    def __init__(self):
        return 

    def caminho_dfs(self, G, s, t, caminho=None):
        if caminho is None:
            caminho = [s]

        if s == t:
            yield caminho

        for proximo in G[s] - set(caminho):
            yield from self.caminho_dfs(G, proximo, t, caminho + [proximo])