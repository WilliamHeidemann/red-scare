from collections import defaultdict
from queue import PriorityQueue
from Graph.Graph import DirectedGraph, Node
from Graph.Parser import Parser

# Oliver's previous implementation, adapted for the problem
def dijkstra(graph: DirectedGraph) -> int:
    dist: defaultdict[Node, int | float] = defaultdict(lambda: float('inf'))
    
    openNodes = PriorityQueue()
    openNodes.put((0, graph.start))

    dist[graph.start] = 0

    while not openNodes.empty():
        currentDistance, node = openNodes.get()

        # we have found the target node
        if node == graph.end:
            return currentDistance

        # we already have a better path here
        if currentDistance > dist[node]:
            continue

        for edge in graph.getNeighbors(node):
            newDistance = currentDistance + edge.cost
            if newDistance < dist[edge.to]:
                openNodes.put((newDistance, edge.to))
                dist[edge.to] = newDistance

    # we never found target
    return -1

def prepareGraphForDijkstra(graph: DirectedGraph) -> DirectedGraph:
    for edges in graph.edges.values():
        for edge in edges:
            if edge.to.red:
                edge.cost = 1
    return graph


# TODO: Get this from parser
parser = Parser("red-scare/data")
graphList = parser.getGraphs()

for graph in graphList:
    graph = prepareGraphForDijkstra(graph)
    redNodes = dijkstra(graph)
    print()