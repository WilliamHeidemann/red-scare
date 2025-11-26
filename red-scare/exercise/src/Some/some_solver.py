from Graph.Graph import DirectedGraph
from Many.many_solver import ManySolver

class SomeSolver:
    def __init__(self, graph: DirectedGraph):
        self.graph = graph

    def solve(self) -> bool:
        return ManySolver(self.graph).solve() > 0
        