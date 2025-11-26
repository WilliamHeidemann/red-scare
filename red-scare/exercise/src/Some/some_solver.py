from Graph.Graph import DirectedGraph
from Many.many_solver import ManySolver

class SomeSolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self) -> bool:
        manyResult = ManySolver(self.graph).solve()
        
        if (manyResult == -2):
            return False
        elif (manyResult == -1):
            return "?"
        
        return True
        