from collections import defaultdict, deque
from dataclasses import dataclass
import sys

sys.setrecursionlimit(1500)


@dataclass(frozen=True)
class Node:
    id: str
    red: bool

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id


@dataclass
class Edge:
    to: Node
    cost: int


class DirectedGraph:
    def __init__(self, redNodes: int, directed: bool = True):
        self.start: Node
        self.end: Node
        self.edges: defaultdict[Node, list[Edge]] = defaultdict(list)
        self.directed: bool = directed
        self.redNodes: int = redNodes

    def addNode(self, node: Node):
        self.edges[node]

    def getNeighbors(self, node: Node):
        return self.edges.get(node, [])

    def addDirectedEdge(self, fromNode: Node, toNode: Node, weight: int = 0):
        self.edges[fromNode].append(Edge(toNode, weight))

    def addUndirectedEdge(self, firstNode: Node, secondNode: Node):
        self.addDirectedEdge(firstNode, secondNode)
        self.addDirectedEdge(secondNode, firstNode)

    def addWeightToEdge(self, fromNode: Node, toNode: Node, weight: int):
        for edge in self.getNeighbors(fromNode):
            if edge.to == toNode:
                edge.cost = weight
                return

    def isCyclic(self) -> bool:
        if self.directed:
            return self.isCyclicDirected()
        else:
            return self.isCyclicUndirected()

    def isCyclicDirected(self) -> bool:
        visited = set()
        in_stack = set()

        def dfs(node):
            visited.add(node)
            in_stack.add(node)

            for edge in self.edges[node]:
                neighbor = edge.to

                if neighbor in in_stack:
                    return True

                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            in_stack.remove(node)
            return False

        return dfs(self.start)

    def isCyclicUndirected(self) -> bool:
        parents: dict[Node, Node] = {}
        queue: deque[Node] = deque()
        queue.append(self.start)
        visited: set[Node] = set()

        while queue:
            current = queue.popleft()
            if current in visited:
                continue

            visited.add(current)

            for edge in self.edges[current]:
                neighbor = edge.to
                if current in parents and neighbor == parents[current]:
                    continue

                if neighbor in visited:
                    return True

                parents[neighbor] = current
                queue.append(neighbor)

        return False
