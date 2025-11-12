# Notes

## Questions for supervision

- How explicit should we be for our NP-hard problems? Should we also try to solve Some for *some* of the graphs.


## Table

| Problem/GraphType | None <br> | Some <br> | Many <br> | Few <br> | Alternate <br> |
|--------------------|-----------------|----------------|-----------------|----------------|----------------------|
| **Return** | Min V | bool | Max V | Min V | bool |
| **Parser (Fabio)** | same | same | same | same | same |
| **Algorithm** | BFS |  | Reduction | Dijkstra | BFS |
| **NP-hard** |  | true | true |  |  |
| **Note** |  |  | Show reduction from some to longest path | add weights for edges to red notes |  |
| **Person** | Filif |  | Will | Oliver | Emil |


## TA Session 12 Nov

- GRAPH TYPES
- directed
- undirected
- directed cyclic
- undirected cyclic

- use a library to check for properties to identify which category a graph belongs to
- check wikipedia on how to solve Longest Path for one of the above for sure (acyclic directed)
- for both NP hardness problems we should be able to solve two of the above categories
