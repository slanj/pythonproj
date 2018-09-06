from test_graph import *

def DFS(graph, start, end, path, shortest):
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def shortestPath(graph, start, end):
    return DFS(graph, start, end, [], None)

if __name__ == "__main__":
    g1 = buildCityGraph()
    print([str(n) for n in shortestPath(g1, g1.getNode("Boston"), g1.getNode("Chicago"))])
