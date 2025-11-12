from src.Graph.Parser import Parser
from src.Graph.Graph import DirectedGraph
from src.NoneSolver.NoneSolver import NoneSolver

class Main:
    parser: Parser = Parser("/Users/philippthiessen/Desktop/algo_design/red-scare/red-scare/data/common-1-20.txt")
    graph: DirectedGraph = parser.createGraph
    solver: NoneSolver = NoneSolver(graph)
    n: int = solver.solve()
    print(n)
