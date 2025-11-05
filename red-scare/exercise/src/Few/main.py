from collections import defaultdict
from queue import PriorityQueue
from Graph.Graph import DirectedGraph, Node

# Oliver's previous implementation, adapted for the problem
def dijkstra(graph: DirectedGraph) -> int:
    dist: defaultdict[Node, int | float] = defaultdict(lambda: float('inf'))
    
    open_nodes = PriorityQueue()
    open_nodes.put((0, graph.start))

    dist[graph.start] = 0

    while not open_nodes.empty():
        current_distance, node = open_nodes.get()

        # we have found the target node
        if node == graph.end:
            return current_distance

        # we already have a better path here
        if current_distance > dist[node]:
            continue

        for edge in graph.getNeighbors(node):
            new_distance = current_distance + edge.cost
            if new_distance < dist[edge.to]:
                open_nodes.put((new_distance, edge.to))
                dist[edge.to] = new_distance

    # we never found target
    return -1

def prepareGraphForDijkstra(graph: DirectedGraph) -> DirectedGraph:
    for edges in graph.edges.values():
        for edge in edges:
            if edge.to.red:
                edge.cost = 1
    return graph


# TODO: Get this from parser
graphList = []

for graph in graphList:
    graph = prepareGraphForDijkstra(graph)
    dijkstra(graph)