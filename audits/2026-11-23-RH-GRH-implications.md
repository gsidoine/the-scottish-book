# Consequences of the November 2026 RH and Dirichlet-GRH formal verification

**Assessment date:** 23 November 2026.

## Verification status and logical scope

On 20 November 2026, Levent Alpöge announced a Lean 4 development of the Riemann hypothesis (RH) and its generalization for Dirichlet $L$-functions, developed with assistance from Claude. On 21 November, the Lean Focused Research Organization and Mathlib Initiative certified that the RH statement and proof had passed independent verification. Andrew Sutherland's verification record reports compilation of 175,187 Lean modules, comparison against Mathlib's pre-existing RH statement, and acceptance by multiple independent proof checkers.

The verified main statements include RH for the Riemann zeta function and the zero-free half-plane $\Re s>1/2$ for every Dirichlet $L$-function, apart from the conventional principal-character pole at $s=1$. This is **Dirichlet GRH**, not GRH for arbitrary automorphic $L$-functions or all Dedekind zeta functions. Independent kernel verification is distinct from human-readable exposition, journal peer review, and formal recognition by a prize body.

Primary sources:
- [Lean FRO and Mathlib Initiative, joint verification statement (21 November 2026)](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/).
- [Andrew Sutherland (MIT), independent verification record (22 November 2026 update)](https://math.mit.edu/~drew/grh/).
- [Alpöge, announcement and development](https://alpo.ge/remark.pdf).

These developments do not change the established mathematical statements or proof statuses in the catalogue merely by association. The effects below distinguish a rigorous standard consequence of RH/GRH from an unproved application to a particular extremal problem.

## P010 — sharpened error term (standard consequence)

The [exact theorem](../theorems/P010-exact-coprime-adjacencies.md) states, for $n\ge4$,

$$
h(n)=\pi(n)-\pi(n/2)+
\max\left(1,\left\lceil\frac{\pi(n/2)-\pi(n/3)}2\right\rceil\right).
$$

Since the last term equals $(\pi(n/2)-\pi(n/3))/2+O(1)$, one has unconditionally

$$
h(n)=\pi(n)-\frac12\pi(n/2)-\frac12\pi(n/3)+O(1).
$$

Under RH, the classical von Koch–Schoenfeld prime-counting estimate gives

$$
\boxed{h(n)=\mathrm{Li}(n)-\frac12\mathrm{Li}(n/2)
-\frac12\mathrm{Li}(n/3)+O(\sqrt n\log n).}
$$

This is a proved *implication from RH*, not a new independent result. It refines the previously recorded first-order asymptotic $h(n)\sim7n/(12\log n)$. The exact finite-$n$ theorem remains unconditional. Neither the new corollary nor RH is part of the existing P010 Lean proof, and the submitted manuscript is unchanged.

Classical reference: [NIST DLMF, §27.12](https://dlmf.nist.gov/27.12) (RH and the prime-counting error bound).

## P033 — prime-sum connectivity (no status change)

The universal result $\kappa(n)\le3$ has an existing unconditional mathematical argument combining effective prime-progression estimates with a finite certificate. Dirichlet GRH offers the classical alternative estimates

$$
\psi(x;q,a)=\frac{x}{\varphi(q)}
+O\!\left(\sqrt{x}\log^2(qx)\right)
$$

for reduced residue classes, with the usual uniformity and normalization conventions. These estimates could yield shorter proofs or improved quantitative ranges, once the constants and the graph-theoretic hypotheses are checked. They do not supersede the unconditional existing proof or its finite certificate without an explicit new derivation.

Neither the P033 full theorem nor this GRH-based analytic chain has been completely formalized in Lean. RH/GRH verification elsewhere does not confer a new Lean certificate on P033.

## P034 — four-prime 2-vertex-connectivity (open)

Dirichlet GRH improves the distribution of *individual* primes in residue classes. It does **not** imply that every sufficiently large interval contains a prime pair with a prescribed fixed gap, or that four selected prime sums form a graph without cut vertices. The universal odd-order four-label problem therefore remains open.

The [unconditional infinite-family result](../theorems/P034-infinitely-many-four-prime-biconnected.md) depends on established bounded prime gaps, an even-order Hamiltonian construction, and a finite arithmetic certificate; it does not require RH or GRH. Its proof and attribution do not change.

A separate structural problem asks for a deterministic 2-connectivity condition for four sum-labels near the midpoint; this, rather than an unproved consequence of GRH, is the relevant graph-theoretic gap.

## Other entries: research consequences and limitations

| Entries | Possible role of RH/Dirichlet GRH | Current implication |
|---|---|---|
| P008, P028 | Improved cancellation for Möbius sums and arithmetic centering, when those sums are identified in the model | No problem resolved; P008 still requires a precise target |
| P032, P037 | Prime counts in short intervals/progressions; for P037, RH bounds classical prime gaps on the relevant scale | Does not prove the proposed exact diameter or a sharp induced-cycle deficit |
| P006, P031, P035 | More precise prime supply for Sidon-type constructions | Does not establish the necessary additive or pairwise-coprime structure |
| P001–P003, P009, P011, P023, P026, P029, P039, P043 | Better prime-counting inputs may assist graph or matching estimates | Structural Hall, connectivity, correlation, or polynomial-prime constraints remain |
| P046, P050 | Stronger global prime-counting errors | Does not control arbitrary binary-XOR correlations or Krawtchouk-weighted prime sums required by the questions |
| P010, P033, P034 | Directly relevant examples treated above | Exact theorem unchanged; stronger asymptotic for P010; no new universal result for P034 |

The remaining entries primarily concern combinatorial reconfiguration, finite-field algebra, topology, random matrices, or geometric and probabilistic phenomena. No direct implication of RH or Dirichlet GRH changes their mathematical status on the information currently established. In particular, neither Goldbach-type prime correlations nor the twin-prime conjecture follows from RH or Dirichlet GRH.

## Repository-level conclusions

1. **No catalogue status is promoted or demoted solely because RH/GRH has been formally verified.** A status change requires a precise implication to the listed problem.
2. The P010 error-term refinement can be recorded as a classical corollary while preserving the unconditional exact theorem and archival manuscript.
3. P033 and P034 retain their existing mathematical statuses. Their potential GRH-based improvements require full arguments rather than references to RH alone.
4. A proof checked in a separate Lean library does not automatically make a corollary Lean-verified. An actual imported theorem and formal deduction, with compatible toolchains and checked axiom dependencies, would be needed to make that claim.
5. Journal publication and human mathematical exposition of the very large RH development are separate from the already completed independent formal proof verification.

This audit is a mathematical consequence assessment, not a new proof of RH or GRH, and makes no claim of priority for classical corollaries.
