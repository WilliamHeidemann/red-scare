from pathlib import Path

from Graph.InputReader import InputReader
from Graph.Graph import DirectedGraph
from Graph.Parser import Parser

# import solvers
from Alternative.alternate_solver import AlternateSolver
from NoneSolver.none_solver import NoneSolver
from Few.few_solver import FewSolver
from Many.many_solver import ManySolver
from Some.some_solver import SomeSolver

# import database
from Database.csv_database import CSVDatabase


def collect_graphs() -> list[tuple[str, DirectedGraph]]:
    files = InputReader.Read()
    graphs: list[tuple[str, DirectedGraph]] = []

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

def run_many_solver(graph):
    solver = ManySolver(graph)
    return solver.solve()

def run_some_solver(graph):
    solver = SomeSolver(graph)
    return solver.solve()

def run_all_solvers(graphs: list[tuple[str, DirectedGraph]]):
    
    db = CSVDatabase("./Database/database.csv")

    for filename, graph in graphs:
        # alternate solver
        result_alt = run_alternate_solver(graph)
        print(f"AlternateSolver: {result_alt}")

        # None solver
        result_none = run_none_solver(graph)
        print(f"NoneSolver: {result_none}")

        # Few solver
        result_few = run_few_solver(graph)
        print(f"FewSolver: {result_few}")

        # Many solver
        result_many = run_many_solver(graph)        
        print(f"ManySolver: {result_many}")

        # Some solver
        result_some = run_some_solver(graph)
        print(f"SomeSolver: {result_some}")

    
        db.addEntry(filename=filename, 
                    V=f"{len(graph.edges)}",
                    Many=f"{result_many}",
                    Some=f"{result_some}",
                    Alternate=f"{result_alt}",
                    No=f"{result_none}",
                    Few=f"{result_few}")


def main():
    graphs = collect_graphs()
    run_all_solvers(graphs)


if __name__ == "__main__":
    main()
