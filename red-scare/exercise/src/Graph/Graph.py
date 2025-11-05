from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Node:
    id: str
    red: bool


@dataclass
class Edge:
    to: Node
    cost: int
    

class DirectedGraph:
    def __init__(self):
        self.nodes: list[Node] = []
        self.edges: defaultdict[Node, list[Edge]] = defaultdict(list)

    def getNeighbors(self, node: Node):
        return self.edges[node]

