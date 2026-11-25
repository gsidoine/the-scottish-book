#!/usr/bin/env python3
"""Exact bounded-span certificate for the P034 four-offset conjecture.

Let D=(-a,-c,e,b), 2<=a, 1<=c<a, 0<=e<b, Q=a+b.
For every Q<=50 with gcd(a-c,a+e,Q)=1, certify that H_(Q-1)(D)
is 2-vertex-connected. A separate elementary extension lemma in
the theorem note then proves this for every m>=Q-1.

This program uses integer arithmetic and ordinary DFS; it does not
assert a symbolic proof for arbitrary Q.
"""
from math import comb, gcd


def biconnected(Q, a, c, e):
    b = Q - a
    m = Q - 1
    n = 2 * m + 1
    adj = [[] for _ in range(n)]
    for k in range(m + 1):
        for d in (-a, -c, e, b):
            j = k + d
            if 0 <= j < m:
                v = m + 1 + j
                adj[k].append(v)
                adj[v].append(k)

    if any(len(neighbors) < 2 for neighbors in adj):
        return False

    discovery = [-1] * n
    low = [0] * n
    parent = [-1] * n
    time = 0
    cut = False

    def visit(u):
        nonlocal time, cut
        discovery[u] = low[u] = time
        time += 1
        children = 0
        for v in adj[u]:
            if discovery[v] == -1:
                parent[v] = u
                children += 1
                visit(v)
                low[u] = min(low[u], low[v])
                if parent[u] != -1 and low[v] >= discovery[u]:
                    cut = True
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])
        if parent[u] == -1 and children > 1:
            cut = True

    visit(0)
    return not cut and time == n


def main():
    certified = 0
    for Q in range(3, 51):
        candidate_count = 0
        for a in range(2, Q):
            b = Q - a
            for c in range(1, a):
                for e in range(b):
                    candidate_count += 1
                    if gcd(a - c, a + e, Q) != 1:
                        continue
                    assert biconnected(Q, a, c, e), (Q, a, c, e)
                    certified += 1
        assert candidate_count == comb(Q, 3), (Q, candidate_count)
    assert certified == 211587, certified
    print(f"P034: all {certified:,} gcd-one critical-span graphs pass (Q<=50).")

    # Independent finite sanity checks for the arbitrary-span explicit family.
    for a in range(2, 71):
        for e in range(70):
            Q = a + e + 1
            assert biconnected(Q, a, a - 1, e), (a, e)
    print("P034: 4,830 consecutive-pair instances also pass (Q up to 140).")


if __name__ == "__main__":
    main()
