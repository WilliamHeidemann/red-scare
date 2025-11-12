### Notes for sub-problem None
- The problem description states that start end end notes can be red
- However, for none, only internal nodes are considered.
- So start and end not could both be red, and we could still find a valid path with no internal red vertices
- v(i) not element of R when 1 < i < l, with 1 and l being start and end indices

### Quick Solver explanation
- The solver performs a simple BFS
- It starts by checking the neighbours of our start node, thereby not caring about the color of that node
- Nodes are valid (and queued) if they are not red or the end node.
- if we reach the end note we return the distance (ie shortest path) if our queue gets empty, we return -1 (no "None" path found)

### Todo

- wait for parser to test/debug/experiment
- set up class that:
    - takes path to data directory
    - loops files (graphs)
        - builds graphs
        - solves None
        - store (in csv?)