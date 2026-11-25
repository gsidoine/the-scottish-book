# P034 — Four prime sums without cut vertices

<!-- DOSSIER-SUMMARY -->
> **Research question:** For every odd n≥7, do four distinct prime sums suffice to make the graph on [n] 2-vertex-connected?  
> **Formulation:** candidate. **Novelty:** unverified; prime-sum connectivity predecessor.  
> **Verified/known progress:** Four labels are optimal for infinitely many odd orders. An elementary arbitrary-span theorem gives 2-connectivity whenever either same-sign offset pair is consecutive; with fixed twin primes 269, 271 and bounded prime gaps it yields a proof of the infinite family without the previous residue certificate.  
> **Finite evidence:** Elementary ear decomposition, with optional 31,980-case (limit 40) or 131,040-case (limit 64) exact checks; 1,498 odd orders through 3001; earlier 6,171-case arithmetic certificate and 211,587 critical-span graph checks.  
> **Symbolic prize:** A Coffee (symbolic) — A construction using four prime sums for every odd order at least seven, or an exceptional order.  
> **Navigation:** [Full problem catalogue](../../README.md#problem-catalogue) · [Status and scope](../../README.md#status-and-scope) · [Literature and audits](../../README.md#literature-and-audits)
<!-- /DOSSIER-SUMMARY -->

**Area:** graph theory and number theory. **Status:** candidate; an infinite family is proved, while the all-odd-order assertion and its historical priority remain unresolved.

## The question

For a set $S$ of odd primes, let $G_n(S)$ have vertex set $[n]$, with an edge between distinct $i,j$ whenever $i+j\in S$. Call a graph **2-vertex-connected** if it has at least three vertices, is connected, and remains connected after any one vertex is deleted.

**P034.** For every odd $n\ge7$, can four distinct prime sums make $G_n(S)$ 2-vertex-connected?

Equivalently, does the minimum number $\kappa_2(n)$ of prime sums giving 2-vertex-connectivity equal **four for every odd $n\ge7$**?

## Rigorous baseline: four are necessary for odd n

For odd $n\ge5$, the sum $n+1$ is even and greater than two, hence is not prime. Every neighbour of vertex 1 produces an odd prime sum $1+j\le n+1$, therefore $1+j\le n$. Every neighbour of vertex n produces an odd prime sum $n+j\ge n+1$, therefore $n+j\ge n+2$. The sets of labels incident to 1 and to n are thus **disjoint**.

In a 2-vertex-connected graph every vertex has degree at least two. Since a fixed sum label determines at most one neighbour of each vertex, two distinct labels are needed at vertex 1 and two **different** labels are needed at vertex n. Hence $\kappa_2(n)\ge4$ for all odd $n\ge5$, whenever $\kappa_2(n)$ is defined.

For even n the lower bound is **not** valid: $n+1$ may be an odd prime and labels at the two endpoint vertices can overlap. For example $n=4$, the palette $\{3,5,7\}$ gives a 4-cycle and is 2-vertex-connected.

The restriction $n\ge7$ is essential: at $n=5$, vertex 5 has only the prime-sum neighbour 2 (because the possible sums are 6,7,8,9,10). Thus no palette of any size can give degree two at vertex 5.

## Infinitely many odd orders

**Theorem (computer-assisted corollary).** There are infinitely many odd integers $n$ with

$$
\boxed{\kappa_2(n)=4.}
$$

The [complete argument](../../theorems/P034-infinitely-many-four-prime-biconnected.md) combines the four-label even-order Hamiltonian construction of Chen–Fu–Guo with the unconditional bounded-prime-gap theorem. If the even-order graph on $[2m]$ has a Hamiltonian cycle using prime sums $a,b,2m+a,2m+b$ with $3\le a<b$, the vertex $2m+1$ attaches to distinct vertices $a-1$ and $b-1$. The resulting odd-order graph is 2-vertex-connected.

For every even gap $g\le246$ and every reduced residue $i$ modulo $g$, an [exact finite computation](../../experiments/P034_infinite_family_verifier.py) produces primes $3\le a\le241$ and $a+g$ satisfying $\gcd(g/2,(i-a)/2)=1$. The $6{,}171$ checked cases remove the possible small-label exception $a=1$ from the even-order construction. This is a finite computation within an unconditional mathematical proof, not an assertion of independent historical novelty.

### An alternative infinite-family proof

The [one-consecutive-pair theorem](../../theorems/P034-one-consecutive-pair-and-prime-gaps.md)
establishes that two consecutive negative offsets suffice for
2-vertex-connectivity at the critical interval length, regardless
of the gap between the two nonnegative offsets. By reflection, the
same holds when only the nonnegative pair is consecutive.

Fix the twin primes $269,271$. For infinitely many prime pairs
$r<s$ with $s-r\le246$, put $n=s-270$. The four sums

$$
269,\quad271,\quad r,\quad s
$$

give a 2-vertex-connected $G_n(S)$ for all sufficiently large such
$n$. The proof uses the unconditional Polymath8b prime-gap theorem
and the explicit spanning ear construction. It does **not** use the
6,171-case modular certificate from the earlier independent proof.
The all-odd-order assertion remains open.

## Finite evidence and witness method

A [self-contained exact verifier](../../experiments/P034_verify_odd_7_to_3001.py) establishes a four-prime 2-vertex-connected palette for each of the $1{,}498$ odd orders $7\le n\le3001$. For each order it examines pairs among the five nearest primes at or below $n$ and the five nearest primes above $n$; at most 11 palettes are tested before finding a witness. The algorithm checks primality and the absence of articulation vertices using integer arithmetic and depth-first low-link values.

Representative witnesses:

| $n$ | Four prime sums |
|---:|---|
| 7 | 5, 7, 11, 13 |
| 39 | 31, 37, 41, 43 |
| 101 | 97, 101, 103, 107 |
| 1001 | 991, 997, 1009, 1013 |
| 2001 | 1997, 1999, 2003, 2011 |
| 3001 | 2999, 3001, 3011, 3019 |

The finite check establishes precisely the stated range; it is not a universal proof.

## Predecessors and novelty risk

The complete prime-sum graph and its Hamiltonian questions have an established literature, including [Chen–Fu–Guo (2021)](https://doi.org/10.1007/s00373-020-02241-1) and [Croot–Jin (2026)](https://doi.org/10.1007/s00373-025-02999-2). The existing [P033](P033-prime-sum-three-palette.md) deals with **connectivity** using three labels; that does not imply 2-vertex-connectivity. The established even-order construction of Chen–Fu–Guo yields the infinite family above, but does not settle every odd order. In particular, central three-sum palettes with one sum above n typically give vertex n degree one.

The remaining question concerns the *sparse-label 2-vertex-connectivity extremum*; the prime-sum graph itself is an established object. A specialist priority check against rainbow/Hamiltonian prime-set literature remains mandatory.

## Interval-reflection reduction

For odd $n=2m+1$, write the odd vertices as $n-2k$ ($0\le k\le m$) and the even vertices as $2j+2$ ($0\le j<m$). A prime sum label $s$ is equivalent to the integer offset

$$
d_s=\frac{s-(n+2)}2.
$$

The edge relation becomes $j-k=d_s$. The [exact graph isomorphism and residue obstruction](../../theorems/P034-four-offset-graph-reduction.md) show that any connected four-label palette must satisfy

$$
\gcd(d_2-d_1,d_3-d_1,d_4-d_1)=1.
$$

The four labels necessarily yield two negative and two nonnegative offsets. Put $Q=d_4-d_1$. The [extension proposition](../../theorems/P034-four-offset-graph-reduction.md#extension-stability) proves that, once $H_m(D)$ is 2-vertex-connected for any $m\ge Q-1$, it remains so for every larger $m$. Thus the statement for all $m\ge Q-1$ is equivalent to its critical case $m=Q-1$.

**Bounded-span theorem (computer-assisted).** If $Q\le50$ and the three offset differences have gcd one, the graph is 2-vertex-connected for **every $m\ge Q-1$**. Its exact [finite certificate](../../experiments/P034_critical_span_certificate.py) verifies all $211{,}587$ qualifying quadruples at the critical size; the extension proposition then covers arbitrarily large $m$. The general critical-span assertion for $Q>50$ remains unproved. There is also an [elementary arbitrary-span family](../../theorems/P034-four-offset-graph-reduction.md#an-unbounded-span-family): for every $a\ge2$ and $e\ge0$, the offsets $\{-a,-a+1,e,e+1\}$ give a 2-vertex-connected graph for all $m\ge a+e$. The proof constructs a cycle through all but one vertex and attaches the remaining vertex to two points of that cycle. This strengthens the earlier finite test of 47,162 width-parameter patterns and does not resolve P034 for all odd $n$.

If the proposed sufficient condition holds in general, the existing P033 prime-palette density theorem implies P034 for **every sufficiently large odd order**, not merely infinitely many odd orders. This is a conditional implication, not a resolution.

## Remaining question

It remains unknown whether $\kappa_2(n)=4$ for **every** odd $n\ge7$. The infinite-family theorem and the finite verification through $n=3001$ do not establish a uniform construction. A counterexample would be an odd order at which every four-prime palette has a cut vertex or is disconnected.

Historical novelty of the universal conjecture requires further specialist comparison with prime-sum Hamiltonicity and bounded-label graph constructions.
