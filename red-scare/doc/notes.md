# Notes

## Questions for supervision

- How explicit should we be for our NP-hard problems? Should we also try to solve Some for *some* of the graphs.


## Table

| Problem/GraphType  | None <br> | Some <br> | Many <br>                                | Few <br>                           | Alternate <br> |
| ------------------ | --------- | --------- | ---------------------------------------- | ---------------------------------- | -------------- |
| **Return**         | Min V     | bool      | Max V                                    | Min V                              | bool           |
| **Parser (Fabio)** | same      | same      | same                                     | same                               | same           |
| **Algorithm**      | BFS       |           | Reduction                                | Dijkstra                           | BFS            |
| **NP-hard**        |           | true      | true                                     |                                    |                |
| **Note**           |           |           | Show reduction from some to longest path | add weights for edges to red notes |                |
| **Person**         | Filif     |           | Will                                     | Oliver                             | Emil           |


## TA Session 12 Nov

- GRAPH TYPES
- directed
- undirected
- directed cyclic
- undirected cyclic

- use a library to check for properties to identify which category a graph belongs to
    - NetworkX - Network Analysis in Python
- check wikipedia on how to solve Longest Path for one of the above for sure (acyclic directed)
- for both NP hardness problems we should be able to solve two of the above categories


## TA Session 19 Nov

- How much do we need to solve for Some?
- How should we argue for our solution for Some? Would it be enough to say: "We did an exhaustive search on small graphs...?"
- Does cyclic matter if we can only do simple paths?
- How do we evaluate our results?

## What we need to do to finish

- Solve sample graphs
- Solver for Many
- Solver for Some
- Finish argument for Many
- Write report
