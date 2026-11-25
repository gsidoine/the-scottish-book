# A consecutive-pair theorem for four-offset graphs

Let $H_m(D)$ denote the bipartite graph with vertices
$A_0,\ldots,A_m$ and $B_0,\ldots,B_{m-1}$, where $A_kB_j$ is an edge
if and only if $j-k\in D$.

## One consecutive pair

**Theorem 1.** Let $a\ge2$, $b\ge1$, and $0\le e<b$, and set

$$
D=\{-a,-a+1,e,b\}.
$$

Then $H_m(D)$ is 2-vertex-connected for every $m\ge a+b-1$.

**Proof.** By the [extension lemma](P034-four-offset-graph-reduction.md#extension-stability), it suffices to take $m=a+b-1$. Write $q=b-e\ge1$.

The three offsets $-a,-a+1,b$ give the path

$$
P:\quad A_{a-1},B_0,A_a,B_1,A_{a+1},\ldots,
B_{b-1},A_{a+b-1},B_b,A_0.
$$

The edge $A_0B_e$ closes the subpath of $P$ from $B_e$ to $A_0$ into
a cycle $C$. The vertices not on $P$ are precisely

$$
A_i,\ B_{b+i}\qquad(1\le i\le a-2).
$$

For every $1\le r\le\min(q,a-2)$, form a path $E_r$ starting at
$B_{e+r}$, visiting the vertices $A_i,B_{b+i}$ in increasing order
$i=r,r+q,r+2q,\ldots<a-1$, and ending at the first $A_t$ with
$t=r+\ell q\ge a-1$. Its consecutive edge offsets alternate between
$e$ and $b$. The internal vertices of different $E_r$ are disjoint,
and together they cover all vertices outside $P$. The initial endpoint
$B_{e+r}$ lies on $C$, and the terminal endpoint $A_t$ lies on $P$.

It remains to adjoin the initial segment of $P$, from $A_{a-1}$
to $B_e$, to the cycle $C$.

If $q\ge a-1$, the additional edge $A_{a-1}B_{e+a-1}$ exists,
since $e+a-1\le b$. The initial segment and this edge form an
ear joining the distinct vertices $B_e$ and $B_{e+a-1}$ of $C$.
Every path $E_r$ now has both endpoints in the resulting
2-vertex-connected subgraph: indeed $t\ge a$ in this case.

If $q\le a-2$, exactly one of the paths $E_r$ terminates at
$A_{a-1}$, namely the path whose initial index $r$ is the
representative of $a-1$ modulo $q$ in $\{1,\ldots,q\}$.
Concatenating this path with the initial segment of $P$ gives
an ear between the distinct vertices $B_e$ and $B_{e+r}$ of $C$.
All other paths $E_r$ then have their endpoints on the completed
spine $P$.

In either case, adjoining the remaining paths $E_r$ as ears yields
a spanning 2-vertex-connected subgraph. Here an ear is a path
whose endpoints are distinct vertices of the existing graph and
whose internal vertices are new; adjoining an ear preserves
2-vertex-connectivity. The extension lemma completes the proof.
$\square$

**Corollary 2 (reflection).** If four offsets have two consecutive
negative entries *or* two consecutive nonnegative entries, with two
offsets on each side of zero, their graph is 2-vertex-connected for
every $m\ge Q-1$, where $Q$ is the difference between the largest and
smallest offsets.

**Proof.** For the second case, reverse the indices of both parts:

$$
A_k\mapsto A_{m-k},\qquad B_j\mapsto B_{m-1-j}.
$$

This replaces every offset $d$ with $-d-1$, interchanging the
negative and nonnegative pairs. The transformed offsets satisfy
Theorem 1. $\square$

The theorem includes the previously recorded
[double-consecutive construction](P034-four-offset-graph-reduction.md#an-unbounded-span-family)
and permits the other pair to have an arbitrary positive gap.
No primality hypothesis is used.

## A simpler infinite-family proof for prime-sum graphs

For a set $S$ of odd primes let $G_n(S)$ be the graph on $[n]$
with edge $xy$ whenever $x\ne y$ and $x+y\in S$.
Let $\kappa_2(n)$ denote the minimum number of labels required
for 2-vertex-connectivity.

**Corollary 3.** There are infinitely many odd integers $n$ such that

$$
\kappa_2(n)=4.
$$

**Proof.** The integers $269$ and $271$ are twin primes. By
Polymath8b's unconditional bounded-gap theorem, there are infinitely
many pairs of primes $r<s$ with $s-r\le246$. For each such pair with
$s$ sufficiently large, put

$$
n=s-270,\qquad S=\{269,271,r,s\}.
$$

Then $n$ is odd, $269<271\le n$, and

$$
n+2\le r<s\le2n-1,
$$

because $s-r\le246<269-1$. Write $n=2m+1$.
The four offsets $d_t=(t-n-2)/2$, for $t\in S$, are

$$
-\frac{n-267}{2},\quad
-\frac{n-267}{2}+1,\quad
134-\frac{s-r}{2},\quad 134.
$$

The first pair is consecutive and negative, while the other
pair is nonnegative. Their span is

$$
Q=\frac{s-269}{2}=\frac{n+1}{2}=m+1.
$$

By Theorem 1 and the [graph isomorphism](P034-four-offset-graph-reduction.md#exact-reduction),
$G_n(S)$ is 2-vertex-connected. These $n$ are distinct for distinct
$s$ and tend to infinity. The endpoint-degree argument in
[P034](../problems/graph-theory/P034-four-prime-sum-biconnectivity.md#rigorous-baseline-four-are-necessary-for-odd-n)
gives $\kappa_2(n)\ge4$ at every odd order for which it is defined,
proving equality. $\square$

For example, $S=\{269,271,997,1009\}$ gives 2-vertex-connectivity
at $n=739$. This finite instance can be checked directly but is
not needed in the proof.

This derives the infinite-family theorem without an *additional*
finite residue certificate or the even-order Hamiltonian construction
used in the [earlier independent proof](P034-infinitely-many-four-prime-biconnected.md).
The all-odd-order conjecture remains open. The deduction does **not** assume infinitely many twin primes: it uses
only the single verified pair $269,271$ and an established bounded-prime-gap
theorem. Polymath8b's published proof has its own analytic and numerical
inputs; the present deduction does not independently verify those inputs.

## References

1. D. H. J. Polymath, [*Variants of the Selberg sieve, and bounded intervals containing many primes*](https://doi.org/10.1186/s40687-014-0012-7), *Research in the Mathematical Sciences* **1** (2014), Article 12. In particular, $H_1\le246$ unconditionally.
2. H.-B. Chen, H.-L. Fu and J.-Y. Guo, [*Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1), *Graphs and Combinatorics* **37** (2021), 209–219. The earlier infinite-family proof uses their construction; the proof above does not.
3. S. Akbari, S. H. Ghorban, S. Malik and S. Qajar, [*Conditions for regularity and for 2-connectivity of Toeplitz graphs*](https://combinatorialpress.com/um/vol110/), *Utilitas Mathematica* **110** (2019), 305–314. This is related structural literature, not a verified exact predecessor to the signed bipartite offset theorem.

No independent historical priority is claimed for the new structural formulation or its prime-sum corollary.
