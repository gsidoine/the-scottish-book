# Four prime-sum labels as an interval bipartite graph

For odd \(n=2m+1\), let \(G_n(S)\) have vertex set \([n]\), with two distinct vertices adjacent when their sum belongs to a set \(S\) of odd integers.

## Exact reduction

For each \(s\in S\) put \(d_s=(s-n-2)/2\), and let \(D=\{d_s:s\in S\}\). Define a bipartite graph \(H_m(D)\) with left vertices \(A_0,\ldots,A_m\), right vertices \(B_0,\ldots,B_{m-1}\), and

\[
A_kB_j\in E(H_m(D))\quad\Longleftrightarrow\quad j-k\in D.
\]

**Proposition 1.** The graphs \(G_n(S)\) and \(H_m(D)\) are isomorphic.

**Proof.** Map \(A_k\) to \(n-2k\) and \(B_j\) to \(2j+2\). These enumerate the odd and even members of \([n]\), respectively. Their sum equals

\[
(n-2k)+(2j+2)=n+2+2(j-k),
\]

so the edge conditions agree. \(\square\)

**Proposition 2 (residue obstruction).** If \(G_n(S)\) is connected, then

\[
\gcd\{d-d_0:d\in D\}=1
\]

for any fixed \(d_0\in D\), provided \(|S|\ge2\).

**Proof.** A two-edge walk \(A_k,B_j,A_\ell\) satisfies \(j-k=d\) and \(j-\ell=d'\), for some \(d,d'\in D\). Hence \(\ell-k=d-d'\). Every walk between left vertices preserves the index modulo the displayed gcd. If the gcd exceeds one, \(A_0\) and \(A_1\) are disconnected. \(\square\)

If four prime labels make \(G_n(S)\) 2-vertex-connected, exactly two of them are at most \(n\), and two are at least \(n+2\). Indeed, vertex \(1\) needs two distinct prime sum labels no larger than \(n\), whereas vertex \(n\) needs two distinct prime sum labels at least \(n+2\). Thus their four offsets have the form

\[
-W\le d_1<d_2<0\le d_3<d_4\le W.
\]

Both the sign pattern and the gcd-one condition are necessary. They are not sufficient without a condition on the interval length. For \(n=7\) and \(S=\{3,5,11,13\}\), the offsets are \((-3,-2,1,2)\) and have gcd-one differences, but \(G_7(S)\) is a spanning path with vertex order \(3,2,1,4,7,6,5\), not a 2-vertex-connected graph. Its endpoints have degree one, and several internal vertices are cut vertices.

## Structural conjecture

**Four-offset criterion (unproved).** Suppose

\[
-W\le d_1<d_2<0\le d_3<d_4\le W,\qquad
\gcd(d_2-d_1,d_3-d_1,d_4-d_1)=1,
\]

where \(W\ge2\). Is \(H_m(\{d_1,d_2,d_3,d_4\})\) 2-vertex-connected for every \(m\ge2W-1\)?

The [finite verifier](../experiments/P034_four_offset_biconnectivity.py) tests all gcd-one offset patterns for each \(2\le W\le12\) and every \(2W-1\le m\le3W+2\), as well as all 34,043 such patterns for \(W=20\) at \(m=39\). No counterexample occurs in these ranges. These tests do not prove the criterion.

## Consequence if the criterion holds

**Proposition 3 (conditional).** The four-offset criterion, together with the established [P033 prime-palette density theorem](P033-prime-palette-density-and-reflection-criterion.md), implies that four distinct prime sums make \(G_n(S)\) 2-vertex-connected for every sufficiently large odd \(n\).

**Proof.** Fix \(0<\delta<1/5\). The P033 density theorem gives, for every sufficiently large odd \(n\), primes \(p<q<n<r\), each within \(\delta n\) of \(n\), with

\[
\gcd((q-p)/2,(r-p)/2)=1.
\]

The prime number theorem supplies another prime \(s\ne r\) in \((n,(1+\delta)n)\). The four offsets associated with \(p,q,r,s\) have exactly two negative and two nonnegative entries and gcd-one differences. Moreover, with \(W=\max|d|\),

\[
W<\frac{\delta n}{2}+1,\qquad m=\frac{n-1}{2}\ge2W-1
\]

for sufficiently large \(n\). The proposed four-offset criterion therefore gives 2-vertex-connectivity. \(\square\)

The universal four-offset criterion has not been proved; Proposition 3 is not a proof of the all-odd-order P034 conjecture. The previously established [infinite-family theorem](P034-infinitely-many-four-prime-biconnected.md) is unconditional and independent of this proposed criterion.
