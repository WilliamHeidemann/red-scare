from collections import defaultdict
from pathlib import Path
from Graph import DirectedGraph, Node

class Parser:
    def __init__(self, path):
        self.path: Path = Path(path)
        

    def loadFiles(self):
        if not self.path.exists() or not self.path.is_dir():
            print("The path is invalid or not a directory.")
            return
    
        files = list(self.path.glob('*.txt'))
        if not files:
            print("No .txt files found in the directory.")
            return
        
        return files
    
    def createGraph(self, file):
        if not file.is_file():
            print(f"Skipping non-file entry: {file}")
            return

        try:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if not lines:
                    print(f"{file.name} is empty.")
                    return

                first_line = lines[0].strip()
                nodesCount, edgesCount, redNodesCount = map(int, first_line.split())
                secondLine = lines[1].strip()
                start, end = secondLine.split()

                #Create the graph
                graph: DirectedGraph = DirectedGraph(start=start, end=end, redNodes=redNodesCount)

                #Get nodes from file
                nodeLines = list(map(str.strip, lines[2: 2 + nodesCount]))
                cachedNodes: defaultdict[str, Node] = defaultdict(list)

                for line in nodeLines:
                    id = line.strip().split()[0]
                    node : Node = Node(id, '*' in line)
                    cachedNodes[id] = node
                    graph.addNode(node)

                if edgesCount <= 0:
                    return graph

                #Get edges from file
                edgeLines = list(map(str.strip, lines[-edgesCount:]))
                directed = '->' in edgeLines[0]

                graph.directed = directed

                for line in edgeLines:
                    start, type, end = line.split()

                    if directed:
                        graph.addDirectedEdge(cachedNodes[start], cachedNodes[end])
                    else:
                        graph.addUndirectedEdge(cachedNodes[start], cachedNodes[end])
                
                return graph 

        except Exception as e:
            print(f"Failed to read {file.name}: {e}")

    def getGraphs(self):
        graphs = []
        files: list = self.loadFiles()

        for file in files:
            graphs.append(self.createGraph(file))

        return graphs
    
if __name__ == "__main__":
    parser = Parser("red-scare/data")
    parser.getGraphs()