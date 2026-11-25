#!/usr/bin/env python3
"""Falsification tests for the unproved P034 four-offset 2-connectivity criterion.

For each width W, test all d1<d2<0<=d3<d4 with -W<=d1 and d4<=W,
and gcd(d2-d1,d3-d1,d4-d1)=1. For W<=12 test every
2W-1 <= m <= 3W+2; for W=20 test m=39.
"""
from itertools import combinations
from math import gcd


def two_connected(m, offsets):
    n = 2 * m + 1
    adj = [[] for _ in range(n)]
    for a in range(m + 1):
        for delta in offsets:
            b = a + delta
            if 0 <= b < m:
                u, v = a, m + 1 + b
                adj[u].append(v)
                adj[v].append(u)
    if any(len(x) < 2 for x in adj):
        return False
    discovery, low, parent = [0] * n, [0] * n, [-1] * n
    clock, cut = 0, False

    def dfs(u):
        nonlocal clock, cut
        clock += 1
        discovery[u] = low[u] = clock
        children = 0
        for v in adj[u]:
            if discovery[v] == 0:
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent[u] != -1 and low[v] >= discovery[u]:
                    cut = True
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])
        if parent[u] == -1 and children > 1:
            cut = True

    dfs(0)
    return not cut and all(discovery)


def main():
    total = 0
    expected = (3, 17, 56, 136, 283, 525, 889, 1421, 2167, 3157, 4465, 34043)
    for W, expected_count in zip((*range(2, 13), 20), expected):
        count = 0
        orders = range(2 * W - 1, 3 * W + 3) if W <= 12 else (2 * W - 1,)
        for lo in combinations(range(-W, 0), 2):
            for hi in combinations(range(0, W + 1), 2):
                offsets = lo + hi
                if gcd(*(d - offsets[0] for d in offsets[1:])) != 1:
                    continue
                count += 1
                for m in orders:
                    assert two_connected(m, offsets), (W, m, offsets)
        assert count == expected_count, (W, count)
        total += count
        print(f"W={W}: {count} gcd-one offset patterns; {len(orders)} orders; pass")
    assert total == 47162
    print(f"PASS: {total} width-parameter pattern tests")


if __name__ == "__main__":
    main()
