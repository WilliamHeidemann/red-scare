from collections import deque
from Graph.Graph import *

class ManySolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self) -> int:
        #if self.graph.directed == False:
        #    return -1
        if self.graph.isCyclic() == True:
            return -1
        
        topological_order = self.topologicallySort()
    
        red_going_to = defaultdict(int)

        for current in topological_order:
            for edge in self.graph.getNeighbors(current):

                neighbor = edge.to

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