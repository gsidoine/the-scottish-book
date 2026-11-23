#!/usr/bin/env python3
"""Exact finite witness search for P034 at every odd order 7 <= n <= 3001.

Only the five nearest primes at most n and the five nearest primes greater
than n are considered. A depth-first low-link test checks connectivity and
absence of articulation vertices for each candidate palette.
"""
from itertools import combinations
from math import isqrt
import sys

sys.setrecursionlimit(10000)


def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p:limit + 1:p] = b"\x00" * ((limit - p * p) // p + 1)
    return sieve


def two_connected(n, labels):
    adj = [[] for _ in range(n + 1)]
    for s in labels:
        for u in range(max(1, s - n), min(n, (s - 1) // 2) + 1):
            v = s - u
            if u < v <= n:
                adj[u].append(v)
                adj[v].append(u)
    if any(len(adj[u]) < 2 for u in range(1, n + 1)):
        return False

    discovery = [0] * (n + 1)
    low = [0] * (n + 1)
    parent = [0] * (n + 1)
    clock = 0

    def dfs(u):
        nonlocal clock
        clock += 1
        discovery[u] = low[u] = clock
        children = 0
        for v in adj[u]:
            if discovery[v] == 0:
                parent[v] = u
                children += 1
                if not dfs(v):
                    return False
                low[u] = min(low[u], low[v])
                if parent[u] != 0 and low[v] >= discovery[u]:
                    return False
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])
        return parent[u] != 0 or children == 1

    return dfs(1) and clock == n


def verify():
    sieve = primes_up_to(6005)
    orders = 0
    max_trials = 0
    for n in range(7, 3002, 2):
        below = [p for p in range(n, 2, -2) if sieve[p]][:5]
        above = [p for p in range(n + 2, 2 * n, 2) if sieve[p]][:5]
        trials = 0
        found = False
        for low_pair in combinations(below, 2):
            for high_pair in combinations(above, 2):
                trials += 1
                labels = low_pair + high_pair
                assert len(set(labels)) == 4 and all(sieve[p] for p in labels)
                if two_connected(n, labels):
                    found = True
                    break
            if found:
                break
        assert found, f"No four-prime witness at n={n}"
        max_trials = max(max_trials, trials)
        orders += 1
    assert orders == 1498 and max_trials == 11
    print(f"PASS: {orders} odd orders 7..3001; at most {max_trials} palettes per order.")


if __name__ == "__main__":
    verify()
