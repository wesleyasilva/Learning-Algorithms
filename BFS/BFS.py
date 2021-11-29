class Bfs(object):
    def __init__(self):
        return

    def bfs(self, graph, s):
        visited,queue = set(),[s]
        while queue:
           vertex = queue.pop(0)
           if vertex not in visited:
               visited.add(vertex)
               queue.extend(graph[vertex]-visited)
        return visited

    def bfs_path(self, graph, s, t):
        queue = [(s, [s])]
        while queue:
            (vertex, way) = queue.pop(0)
            for nextt in graph[vertex] - set(way):
                if nextt == t:
                    yield way + [nextt]
                else:
                    queue.append((nextt, way + [nextt]))

    def shortest_path(self, graph, s, t):
        try:
            return self.bfs_path(graph, s, t)
        except StopIteration:
            return None
