class Dfs(object):
    def __init__(self):
        return 

    def dfs_path(self, G, s, t, path=None):
        if path is None:
            path = [s]

        if s == t:
            yield path

        for nextt in G[s] - set(path):
            yield from self.dfs_path(G, nextt, t, path + [nextt])
