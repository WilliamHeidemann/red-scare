# Notes on longest path (LP)
- Is NP-hard
- Graphs with cycles may have paths with infinite length
- If the graph does not have cycles, the longest path can be found like this:
    - Find P, the set of s, t-paths. Time complexity: O(n!)
    - Return max{ |p|: p ∈ P }.
- Graphs with <20 vertices can be brute forced
    - Algorithm: 
    - DFS with dynamic programming (memoisation). 
    - Explore all possible paths. 
    - O(n!) 
- Longest path can be solved in O(n) on acyclic directed graphs


# Notes on Many
- A maximizing problem (like LP)
- Longer paths can contain more red vertices.
- let r(p) = the number of red vertices of a path
- To solve it:
    - Find P, the set of s, t-paths. Time complexity: O(n!)
    - Let r(p) denote the number of red vertices on a path p. 
    - Return max{ r(p): p ∈ P }.
