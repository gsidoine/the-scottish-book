#!/usr/bin/env python3
"""Check the explicit ear construction for P034's one-consecutive-pair theorem.

The mathematical proof is independent of the finite tests.
Run with --limit 64 to check the 131,040 triples with
2 <= a <= 64, 1 <= b <= 64 and 0 <= e < b.
"""
import argparse

def verify(a, b, e):
    assert a >= 2 and b >= 1 and 0 <= e < b
    q, m = b - e, a + b - 1
    offsets = {-a, -a + 1, e, b}
    vertices = ({("A", k) for k in range(m + 1)} |
                {("B", j) for j in range(m)})

    def edge(x, y):
        if x[0] == "A" and y[0] == "B":
            return y[1] - x[1] in offsets
        if x[0] == "B" and y[0] == "A":
            return x[1] - y[1] in offsets
        return False

    def path_ok(path):
        assert len(path) == len(set(path)), (a, b, e, "repeat")
        assert all(edge(x, y) for x, y in zip(path, path[1:])), (
            a, b, e, "invalid edge")

    spine = [("A", a - 1)]
    for j in range(b):
        spine += [("B", j), ("A", a + j)]
    spine += [("B", b), ("A", 0)]
    path_ok(spine)

    cut = spine.index(("B", e))
    cycle = spine[cut:]
    path_ok(cycle)
    assert edge(cycle[-1], cycle[0])
    used = set(cycle)
    ears = []
    for r in range(1, min(q, a - 2) + 1):
        path = [("B", e + r)]
        i = r
        while i <= a - 2:
            path += [("A", i), ("B", b + i)]
            i += q
        path.append(("A", i))
        path_ok(path)
        ears.append((r, path))

    initial = list(reversed(spine[:cut + 1]))
    assert initial[0] == ("B", e)
    if q >= a - 1:
        extra = initial + [("B", e + a - 1)]
    else:
        r, special = next((r, path) for r, path in ears
                          if path[-1] == ("A", a - 1))
        extra = initial + list(reversed(special))[1:]
        ears = [(s, path) for s, path in ears if s != r]
    path_ok(extra)
    assert extra[0] in used and extra[-1] in used
    assert extra[0] != extra[-1]
    assert not (set(extra[1:-1]) & used)
    used.update(extra[1:-1])
    for _, path in ears:
        assert path[0] in used and path[-1] in used
        assert path[0] != path[-1]
        assert not (set(path[1:-1]) & used)
        used.update(path[1:-1])
    assert used == vertices, (a, b, e, "incomplete spanning cover")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()
    assert args.limit >= 2
    total = 0
    for a in range(2, args.limit + 1):
        for b in range(1, args.limit + 1):
            for e in range(b):
                verify(a, b, e)
                total += 1
    assert total == (args.limit - 1) * args.limit * (args.limit + 1) // 2
    from P034_verify_odd_7_to_3001 import two_connected
    assert two_connected(739, (269, 271, 997, 1009))
    print(f"PASS: {total:,} exact ear decompositions; "
          "prime-sum witness n=739 also biconnected")


if __name__ == "__main__":
    main()
