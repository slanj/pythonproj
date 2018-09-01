'''
The teacher only swaps the positions of two students that are next to each other.
Let's consider a line of three students, Alice, Bob, and Carol
(denoted A, B, and C). Using the Graph class created in the lecture,
we can create a graph with the design chosen in Exercise 1:
vertices represent permutations of the students in line;
edges connect two permutations if one can be made into the other by swapping
two adjacent students.
Add the appropriate edges to the graph.
'''

from graph import *

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

for node1 in nodes:
    for node2 in nodes:
        if node1.getName() == node2.getName():
            continue
        correct = 0
        for letter in node1.getName():
            if node1.getName().find(letter) == node2.getName().find(letter) or node1.getName().find(letter) == (node2.getName().find(letter) + 1) or node1.getName().find(letter) == (node2.getName().find(letter) - 1):
                correct += 1
        if correct == 3:
             Digraph.addEdge(g, Edge(node1, node2))

print([str(i) for i in g.childrenOf(g.getNode("ABC"))])
print(g)
