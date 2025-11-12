# Claim: Many is NP-hard

Proof. We will reduce from Longest Path, which is known to be NP-hard.

Let G be an instance of Longest Path problem. Enumerate the vertex set of G as V = {v_1, ..., v_n}. Enumerate the edge set of G as E = {e_1, ..., e_m}. Every edge is directed and points from u to v and has some edge weight w(e). 

Construct an instance G, V, E, R, B of Many as follows. Enumerate vertex set V(G) and edge set E(G) like before. Enumerate red set R(V) where R ⊆ V(G). Enumerate the black set to be the remaining nodes B(V) ⊆ V(G) = V(G) - R(V).
Set the weight of every edge e based on the color of the end vertex v. If v ∈ B(V) then w(e) = 0. If v ∈ R(V) then w(e) = 1.

For example, if G_example is an instance to Longest Path 

![G_example.img](LongestPathExampleGraph.png)

then the resulting instance to Many is 

![G_red_example.img](ManyExampleGraph.png)

(Note that the resulting instance is size O(|V|+|E|), which is polynomial in the size of G.) 

Now let p ∈ P be a solution to Many for the instance. In other words the path p has the highest number of red vertices possible within a path from s to t. Then the corresponding path from s to t in Longest Path has maximum length in terms of edge weights. 

Conversely, if p ∈ P is a solution to Longest Path with maximum length, then the corresponding path s to t in Many has the highest number of red vertices possible within a path from s to t.