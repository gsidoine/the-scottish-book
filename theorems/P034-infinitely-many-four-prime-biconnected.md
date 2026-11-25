# Four prime sums give 2-vertex-connectivity infinitely often

**Status:** unconditional, computer-assisted corollary of Chen–Fu–Guo's Hamiltonian construction and the Polymath8b bounded-prime-gap theorem. It does not settle the [all-odd-order question](../problems/graph-theory/P034-four-prime-sum-biconnectivity.md).

For a finite set of primes $S$, let $G_n(S)$ be the graph on $[n]$ in which distinct $x,y$ are adjacent precisely when $x+y\in S$. Write $\kappa_2(n)$ for the smallest size of $S$ making $G_n(S)$ 2-vertex-connected, when such a set exists.

**Theorem.** There are infinitely many odd integers $n$ for which

$$
\boxed{\kappa_2(n)=4.}
$$

### Alternative proof without a finite residue certificate

An [independent elementary construction](P034-one-consecutive-pair-and-prime-gaps.md)
proves the same infinite-family theorem using one fixed twin-prime pair,
$269,271$, and the Polymath8b bound $246$ for infinitely recurring prime
gaps. It does not use the finite arithmetic lemma below or the
even-order Hamiltonian construction of Chen–Fu–Guo.

The argument below is preserved as a separate, computer-assisted proof
with its own explicit mathematical dependencies and certificate.

### Hamiltonian-cycle extension

**Lemma 1.** Let $m\ge2$ and let $3\le a<b\le2m$ be primes such that $2m+a$ and $2m+b$ are prime and

$$
\gcd\left(\frac{b-a}{2},m\right)=1.
$$

Then $G_{2m+1}(S)$ is 2-vertex-connected for $S=\{a,b,2m+a,2m+b\}$.

**Proof.** Theorem 1.3 of Chen–Fu–Guo gives a Hamiltonian cycle in $G_{2m}(S)$. The vertex $2m+1$ has distinct neighbors $a-1$ and $b-1$ because

$$
(2m+1)+(a-1)=2m+a,\qquad
(2m+1)+(b-1)=2m+b.
$$

Both neighbors belong to $[2m]$. Deleting the new vertex leaves the Hamiltonian cycle; deleting an old vertex leaves a connected Hamiltonian path to which the new vertex remains adjacent. Thus $G_{2m+1}(S)$ is 2-vertex-connected. $\square$

### Finite arithmetic lemma

**Lemma 2 (exact finite verification).** For every even integer $g$ with $2\le g\le246$ and every $i\in\{1,\ldots,g-1\}$ satisfying $\gcd(i,g)=1$, there is a prime $a$, $3\le a\le241$, such that $a+g$ is prime and

$$
\gcd\left(\frac g2,\frac{i-a}{2}\right)=1.
$$

**Verification.** The [standard-library verifier](../experiments/P034_infinite_family_verifier.py) enumerates all $6{,}171$ reduced-residue cases, checks primality by trial division, and finds a witness in each case. The greatest least witness is $a=241$, attained for $(g,i)=(148,35)$, where $a+g=389$. No probabilistic test or external numerical table is required. This is a finite computer-assisted lemma, not a symbolic Lean proof.

### Proof of the theorem

The unconditional bounded-prime-gap theorem gives infinitely many pairs of primes $R<R+g$ for some fixed even $g\le246$. By passing to an infinite subsequence, one may fix $R\equiv i\pmod g$, where $\gcd(i,g)=1$. Choose the primes $a$ and $b=a+g$ from Lemma 2. For sufficiently large $R$, put

$$
2m=R-a.
$$

Then $3\le a<b\le2m$, and $2m+a=R$ and $2m+b=R+g$ are prime. Moreover,

$$
\gcd\left(\frac{b-a}{2},m\right)
=\gcd\left(\frac g2,\frac{R-a}{2}\right)
=\gcd\left(\frac g2,\frac{i-a}{2}\right)=1.
$$

Lemma 1 supplies four prime labels making $G_{2m+1}$ 2-vertex-connected. Since $R$ ranges over infinitely many distinct primes, so does the odd integer $2m+1$. For odd $n$, at least two distinct prime sums are needed at vertex $1$ and two further sums at vertex $n$: the former labels are at most $n$ and the latter are at least $n+2$. Hence $\kappa_2(n)\ge4$, proving equality. $\square$

### References

1. H.-B. Chen, H.-L. Fu and J.-Y. Guo, [*Hamiltonicity in Prime Sum Graphs*](https://doi.org/10.1007/s00373-020-02241-1), *Graphs and Combinatorics* **37** (2021), 209–219, Theorem 1.3.
2. D. H. J. Polymath, [*Variants of the Selberg sieve, and bounded intervals containing many primes*](https://doi.org/10.1186/s40687-014-0012-7), *Research in the Mathematical Sciences* **1** (2014), Article 12. In particular, $\liminf (p_{k+1}-p_k)\le246$.

The result is an explicit corollary of established prime-gap and Hamiltonicity theorems together with a finite arithmetic certificate. No claim of independent historical novelty is made.
