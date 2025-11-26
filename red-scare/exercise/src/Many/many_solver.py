from collections import deque
from Graph.Graph import *

class ManySolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self):
        if self.graph.directed:
            return self.solveDirected()
        else:
            return self.solveUndirected()
        
 
    def solveUndirected(self) -> int:
        if self.graph.isCyclic():
            return -1

        parents: dict[Node, Node] = {}
        red_counts: defaultdict[Node, int] = defaultdict(int)
        queue: deque[Node] = deque([self.graph.start])
        visited = {self.graph.start}
        red_counts[self.graph.start] = 1 if self.graph.start.red else 0

        while queue:
            current = queue.popleft()

            for edge in self.graph.edges[current]:
                neighbor = edge.to
                parent = parents.get(current)
                if parent is not None and neighbor == parent:
                    continue
                
                if neighbor == self.graph.end:
                    return red_counts[current] + (1 if neighbor.red else 0)

                if neighbor not in visited:
                    parents[neighbor] = current
                    red_counts[neighbor] = red_counts[current] + (1 if neighbor.red else 0)
                    visited.add(neighbor)
                    queue.append(neighbor)

        return -2
    

    def solveDirected(self) -> int:
        if self.graph.isCyclic():
            return -1
        
        topological_order = self.topologicallySort()
    
        red_going_to = defaultdict(int)

        for current in topological_order:
            for edge in self.graph.getNeighbors(current):

                neighbor = edge.to

                if neighbor == current:
                    continue

                if neighbor.red:
                    red_from_current = red_going_to[current] + 1
                else:
                    red_from_current = red_going_to[current]

                red_going_to[neighbor] = max(red_going_to[neighbor], red_from_current)

                if neighbor == self.graph.end:
                    return red_going_to[neighbor]
                
        return -2
    
    def topologicallySort(self):
        visited = set()
        queue = deque()
        queue.append(self.graph.start)

        sorted = []

        while(len(queue) > 0): 
            node = queue.popleft()

            if (node in visited): 
                continue

            visited.add(node)
            sorted.append(node)
            for neighbor in self.graph.getNeighbors(node):
                queue.append(neighbor.to)

        return sorted