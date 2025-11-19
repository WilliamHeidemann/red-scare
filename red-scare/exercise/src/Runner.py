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
#from Database.csv_database import CSVDatabase


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

def run_many_solver(graph):
    solver = ManySolver(graph)
    return solver.solve()

def run_all_solvers(graphs: list[tuple[str, object]]):
    #db = CSVDatabase("./Database/database.csv")


    cyclic = 0
    solved = 0
    for filename, graph in graphs:
        # alternate solver
        #result_alt = run_alternate_solver(graph)
        #print(f"AlternateSolver: {result_alt}")

        # None solver
        #result_none = run_none_solver(graph)
        #print(f"NoneSolver: {result_none}")

        # Few solver
        #result = run_few_solver(graph)
        #print(f"FewSolver: {result}")

        # Many solver
        result = run_many_solver(graph)
        if result == -1:
            cyclic += 1
        else:
            solved += 1
        print(f"ManySolver: {result} - {filename}")
    
    print(f"Cyclic: {cyclic}")
    print(f"Solved: {solved}")

        #db.addEntry(filename=filename, No=f"{result_none}", Alternate=f"{result_alt}")


def main():
    graphs = collect_graphs()
    run_all_solvers(graphs)


if __name__ == "__main__":
    main()
