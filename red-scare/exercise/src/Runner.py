from pathlib import Path

from Graph.InputReader import InputReader
from Graph.Graph import DirectedGraph
from Graph.Parser import Parser

# import solvers
from Alternative.alternate_solver import AlternateSolver
from NoneSolver.none_solver import NoneSolver
from Few.few_solver import FewSolver




def collect_graphs() -> list[tuple[str, object]]:
    files = InputReader.Read()
    graphs: list[tuple[str, object]] = []

    for p in files:
        graph = Parser.createGraph(p)
        if graph is not None:
            graphs.append((p.name, graph))

    return graphs

# functions for each solver
def run_alternate_solver(graph):
    solver = AlternateSolver(graph)
    return solver.solve()


def run_none_solver(graph):
    solver = NoneSolver(graph)
    return solver.solve()


def run_few_solver(graph):
    solver = FewSolver(graph)
    return solver.solve()


def run_all_solvers(graphs: list[tuple[str, object]]):
    for filename, graph in graphs:
        # alternate solver
         result = run_alternate_solver(graph)
         print(f"AlternateSolver: {result}")

        # None solver
        #result = run_none_solver(graph)
        #print(f"NoneSolver: {result}")

        # Few solver
        # result = run_few_solver(graph)
        # print(f"FewSolver: {result}")


def main():
    graphs = collect_graphs()
    run_all_solvers(graphs)


if __name__ == "__main__":
    main()