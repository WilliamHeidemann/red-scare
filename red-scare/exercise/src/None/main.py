from collections import deque
from Graph.Graph import DirectedGraph

class NoneSolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self) -> int:
        """
        Return the length of the shortest path from start to end,
        avoiding internal red nodes, or -1 if path does not exists.
        """
        startNode = self.graph.start
        endNode = self.graph.end

        # (node, path_length)
        queue = deque([(startNode, 0)])
        visited = {startNode}

        while queue:
            current_node, distance = queue.popleft()

            # end reached, shortest path found
            if current_node == endNode:
                return distance

            # Explore neighbors
            for edge in self.graph.getNeighbors(current_node):
                neighbor_node = edge.to

                if neighbor_node not in visited:
                    # path is valid if neighbor is not red OR end node
                    if not neighbor_node.red or neighbor_node == endNode:
                        visited.add(neighbor_node)
                        queue.append((neighbor_node, distance + 1))
        
        # queue empty, no path found
        return -1
