# Notes about the Few problem

In this problem, we should return the minimum number of red vertices we have to visit on a path from $s$ to $t$.

The problem can be reduced to an instance of the weighted shortest path problem. By taking the input as a graph and converting it to a directed weighted graph, we can put the cost of 0 on all edges going into black vertices and a cost of 1 on all edges going into red vertices.

Although, my intuition told me that this might result in too many edges being taken, since a black edge is essentially for free, so it does not know the optimal way and just chooses randomly.

According to [this stackoverflow post](https://stackoverflow.com/questions/49460439/can-dijkstras-algorithm-work-on-a-graph-with-weights-of-0), on an "all-zero" graph Dijkstra would essentially become a breath-first-search, guaranteeing the shortest path.

Therefore, the path returned by Dijkstra would be the shortest path if there is one without red vertices. It would also return the one with the lowest amount of red vertices, since they cost more than the other edges, meaning that Dijkstra will take a path without it, no matter how many black vertices it has to visit.
