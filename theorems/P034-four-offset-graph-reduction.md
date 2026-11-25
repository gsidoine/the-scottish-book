# Four prime-sum labels as an interval bipartite graph

For odd $n=2m+1$, let $G_n(S)$ have vertex set $[n]$, with two distinct vertices adjacent when their sum belongs to a set $S$ of odd integers.

## Exact reduction

For each $s\in S$ put $d_s=(s-n-2)/2$, and let $D=\{d_s:s\in S\}$. Define a bipartite graph $H_m(D)$ with left vertices $A_0,\ldots,A_m$, right vertices $B_0,\ldots,B_{m-1}$, and

$$
A_kB_j\in E(H_m(D))\quad\Longleftrightarrow\quad j-k\in D.
$$

**Proposition 1.** The graphs $G_n(S)$ and $H_m(D)$ are isomorphic.

**Proof.** Map $A_k$ to $n-2k$ and $B_j$ to $2j+2$. These enumerate the odd and even members of $[n]$, respectively. Their sum equals

$$
(n-2k)+(2j+2)=n+2+2(j-k),
$$

so the edge conditions agree. $\square$

**Proposition 2 (residue obstruction).** If $G_n(S)$ is connected, then

$$
\gcd\{d-d_0:d\in D\}=1
$$

for any fixed $d_0\in D$, provided $|S|\ge2$.

**Proof.** A two-edge walk $A_k,B_j,A_\ell$ satisfies $j-k=d$ and $j-\ell=d'$, for some $d,d'\in D$. Hence $\ell-k=d-d'$. Every walk between left vertices preserves the index modulo the displayed gcd. If the gcd exceeds one, $A_0$ and $A_1$ are disconnected. $\square$

If four prime labels make $G_n(S)$ 2-vertex-connected, exactly two of them are at most $n$, and two are at least $n+2$. Indeed, vertex $1$ needs two distinct prime sum labels no larger than $n$, whereas vertex $n$ needs two distinct prime sum labels at least $n+2$. Thus their four offsets have the form

$$
-W\le d_1<d_2<0\le d_3<d_4\le W.
$$

Both the sign pattern and the gcd-one condition are necessary. They are not sufficient without a condition on the interval length. For $n=7$ and $S=\{3,5,11,13\}$, the offsets are $(-3,-2,1,2)$ and have gcd-one differences, but $G_7(S)$ is a spanning path with vertex order $3,2,1,4,7,6,5$, not a 2-vertex-connected graph. Its endpoints have degree one, and several internal vertices are cut vertices.

## Related finite Toeplitz graphs

The bipartite incidence matrix of $H_m(D)$ has four constant diagonals. Closely related literature includes S. Nicoloso and U. Pietropaoli, [*Bipartite finite Toeplitz graphs*](https://doi.org/10.1016/j.dam.2013.05.020), *Discrete Applied Mathematics* **165** (2014), 233–244, and S. Akbari, S. Hossein Ghorban, S. Malik and S. Qajar, [*Conditions for regularity and for 2-connectivity of Toeplitz graphs*](https://combinatorialpress.com/um/vol110/), *Utilitas Mathematica* **110** (2019), 305–314. The standard finite Toeplitz graph uses undirected absolute differences; $H_m(D)$ uses a rectangular bipartite incidence matrix with signed offsets. No equivalence with the present critical-span assertion has been established. Neither the change of coordinates nor the general theory of Toeplitz graphs is claimed as new.

## Extension stability

Write $D=\{d_1,d_2,d_3,d_4\}$ with

$$
d_1<d_2<0\le d_3<d_4,\qquad Q=d_4-d_1.
$$

**Proposition (extension).** For every $m\ge Q-1$,

$$
H_m(D)\text{ is 2-vertex-connected}
\ \Longrightarrow\
H_{m+1}(D)\text{ is 2-vertex-connected}.
$$

**Proof.** The old graph is an induced subgraph of the new graph. Add $B_m$ first. It has the two distinct old neighbors $A_{m-d_3}$ and $A_{m-d_4}$, because $m\ge Q-1\ge d_4$. Then add $A_{m+1}$. It has two distinct neighbors $B_{m+1+d_1}$ and $B_{m+1+d_2}$ in the enlarged graph. Both indices lie between $0$ and $m$, and $d_1\le-2$, so the first is an old right vertex. Adding a vertex adjacent to two distinct vertices of a 2-vertex-connected graph preserves 2-vertex-connectivity. Applying this twice proves the claim. $\square$

**Corollary (critical-size reduction).** For every fixed $D$ as above,

$$
H_m(D)\text{ is 2-vertex-connected for all }m\ge Q-1
\quad\Longleftrightarrow\quad
H_{Q-1}(D)\text{ is 2-vertex-connected}.
$$

This equivalence requires no coprimality hypothesis. The bound $Q-1$ is sharp as a uniform lower threshold: for $D=\{-3,-2,0,2\}$ one has $Q=5$; $H_3(D)$ has a vertex $A_1$ of degree one, while $H_4(D)$ is 2-vertex-connected.

## A bounded-span theorem

**Theorem (computer-assisted).** Suppose

$$
d_1<d_2<0\le d_3<d_4,\qquad
Q=d_4-d_1\le50,\qquad
\gcd(d_2-d_1,d_3-d_1,d_4-d_1)=1.
$$

Then $H_m(D)$ is 2-vertex-connected for every $m\ge Q-1$.

**Proof.** Write $D=\{-a,-c,e,b\}$, where $2\le a$, $1\le c<a$, $0\le e<b$, and $Q=a+b$. The gcd condition becomes

$$
\gcd(a-c,a+e,Q)=1.
$$

The [exact finite verifier](../experiments/P034_critical_span_certificate.py) enumerates every $3\le Q\le50$, $2\le a<Q$, $1\le c<a$ and $0\le e<Q-a$. It tests the gcd condition and checks 2-vertex-connectivity of $H_{Q-1}(D)$ using integer arithmetic and an articulation-point depth-first search. All $211{,}587$ gcd-one instances pass; the number of quadruples examined at each fixed $Q$ before gcd filtering is $\binom Q3$. The extension proposition completes the proof for every $m\ge Q-1$. $\square$

The finite verification is a component of the proof; it is not a symbolic proof for arbitrary $Q$. An independent NetworkX implementation agreed on 300 randomly sampled test cases.

## Structural conjecture

**Critical-span conjecture (unproved).** For every four integers $d_1<d_2<0\le d_3<d_4$ whose differences have gcd one, is $H_{Q-1}(D)$ 2-vertex-connected, where $Q=d_4-d_1$?

By the extension proposition this would also hold for every $m\ge Q-1$. It is stronger than the earlier sufficient-condition candidate $m\ge2W-1$ when $D\subseteq[-W,W]$, because $Q\le2W$. No proof or counterexample for arbitrary $Q$ is established here.

## Consequence if the criterion holds

**Proposition 3 (conditional).** The four-offset criterion, together with the established [P033 prime-palette density theorem](P033-prime-palette-density-and-reflection-criterion.md), implies that four distinct prime sums make $G_n(S)$ 2-vertex-connected for every sufficiently large odd $n$.

**Proof.** Fix $0<\delta<1/5$. The P033 density theorem gives, for every sufficiently large odd $n$, primes $p<q<n<r$, each within $\delta n$ of $n$, with

$$
\gcd((q-p)/2,(r-p)/2)=1.
$$

The prime number theorem supplies another prime $s\ne r$ in $(n,(1+\delta)n)$. The four offsets associated with $p,q,r,s$ have exactly two negative and two nonnegative entries and gcd-one differences. Moreover, with $W=\max|d|$,

$$
W<\frac{\delta n}{2}+1,\qquad m=\frac{n-1}{2}\ge2W-1
$$

for sufficiently large $n$. The proposed four-offset criterion therefore gives 2-vertex-connectivity. $\square$

The universal four-offset criterion has not been proved; Proposition 3 is not a proof of the all-odd-order P034 conjecture. The previously established [infinite-family theorem](P034-infinitely-many-four-prime-biconnected.md) is unconditional and independent of this proposed criterion.
