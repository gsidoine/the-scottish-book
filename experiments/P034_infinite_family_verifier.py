#!/usr/bin/env python3
"""Exact finite arithmetic lemma for four-prime-sum 2-vertex-connectivity.

For every even gap 2 <= g <= 246 and every i coprime to g,
find primes 3 <= a <= 241 and a+g with gcd(g/2, (i-a)/2) = 1.
Only integer arithmetic and trial division are used.
"""
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def verify():
    cases = 0
    largest_witness = (0, 0, 0, 0)
    for g in range(2, 247, 2):
        pairs = [(a, a + g) for a in range(3, 242, 2)
                 if prime(a) and prime(a + g)]
        for i in range(1, g, 2):
            if gcd(i, g) != 1:
                continue
            witness = next((a for a, b in pairs
                            if gcd(g // 2, (i - a) // 2) == 1), None)
            assert witness is not None, (g, i)
            assert prime(witness) and prime(witness + g)
            if witness > largest_witness[2]:
                largest_witness = (g, i, witness, witness + g)
            cases += 1
    assert cases == 6171, cases
    assert largest_witness == (148, 35, 241, 389), largest_witness
    print(f"PASS: {cases} cases; largest least witness: {largest_witness}")


if __name__ == "__main__":
    verify()
