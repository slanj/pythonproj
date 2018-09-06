from test_graph import *

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPath(pathQueue))
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
        print('pathQueue:', printPath2(pathQueue))
    return None

def printPath(path):
    return ([str(n) for n in path])

def printPath2(path):
    inpath = []
    for n in path:
        tempstr = '['
        for nn in n:
            tempstr += str(nn) + " "
        tempstr += ']'
        inpath.append(tempstr)
        tempstr = ""
    return ([str(n) for n in inpath])

g1 = buildCityGraph()

BFS(g1, g1.getNode("Boston"), g1.getNode("Phoenix"))







