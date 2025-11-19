from collections import deque
from Graph.Graph import DirectedGraph

class AlternateSolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self) -> bool:
        
        startNode = self.graph.start
        endNode = self.graph.end

        # queue
        queue = deque([startNode])
        visited = {startNode}

        while queue:
            current = queue.popleft()

            # end reached path exists
            if current == endNode:
                return True

            for edge in self.graph.getNeighbors(current):
                neighbour = edge.to

                if neighbour in visited:
                    continue

                # only traverse if different colors
                if neighbour.red == current.red:
                    continue

                visited.add(neighbour)
                queue.append(neighbour)

        # no path found
        return False