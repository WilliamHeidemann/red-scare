# Claim: Many is NP-hard

Proof. We will reduce from the Hamiltonian Path problem, which is known to be NP-Hard.

Let G be an instance of the Hamiltonian Path problem. Enumerate the vertex set of G as V = {v_1, ..., v_n}. Enumerate the edge set of G as E = {e_1, ..., e_m}.

Construct an instance G, V, E, R, B, s, t of Many as follows. Enumerate the vertex set V(G) and E(G) like before. Color every vertex red. In particular R(G) = V(G) and B(G) = empty set. Let s be arbitrarily assigned from the set of vertices V(G). Let t be a vertex such that there exists an edge from s to t in E(G).

For example, if this is an instance to Hamiltonian Path

![G_example.img](LongestPathExampleGraph.png)

then the resulting instance to Many is

![G_red_example.img](ManyExampleGraph.png)

(Note that the resulting instance is size O(|V|+|E|), which is polynomial in the size of G.)

Now let p ∈ P be a solution to Many for the instance. In other words the path p has the highest number of red vertices possible within a path from s to t. If number of red vertices returned by many is equal to |V|, then there is a Hamiltonian Path.

Conversely, if p ∈ P is a solution to Hamiltonian Path, then the corresponding path s to t in Many has the highest number of red vertices possible within a path from s to t.
