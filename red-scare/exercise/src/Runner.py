from pathlib import Path

from Graph.InputReader import InputReader
from Graph.Graph import DirectedGraph
from Graph.Parser import Parser

# import solvers
from Alternative.alternate_solver import AlternateSolver
from NoneSolver.none_solver import NoneSolver
from Few.few_solver import FewSolver
from Many.many_solver import ManySolver

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

def run_all_solvers(graphs: list[tuple[str, DirectedGraph]]):
    
    db = CSVDatabase("./Database/database.csv")

    cyclic_directed = 0
    cyclic_undirected = 0
    acyclic_undirected = 0
    acyclic_directed = 0
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
        if graph.directed:
            if graph.isCyclic():
                cyclic_directed += 1
            else:
                acyclic_directed += 1
        else:
            if graph.isCyclic():
                cyclic_undirected += 1
            else:
                acyclic_undirected += 1
                
        result_many = run_many_solver(graph)
        
        print(f"ManySolver: {result_many} - {filename}")
    
        db.addEntry(filename=filename, 
                    Many=f"{result_many}",
                    Alternate=f"{result_alt}",
                    No=f"{result_none}",
                    Few=f"{result_few}")


def main():
    graphs = collect_graphs()
    run_all_solvers(graphs)


if __name__ == "__main__":
    main()
