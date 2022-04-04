from typing import List
from collections import defaultdict


def get_best(n: int, F: List[int], P: List[int]) -> int:
    F = [-1] + F
    P = [-1] + P

    nodes = range(n+1)
    nodes = sorted(nodes, key=lambda x: P[x], reverse=True)

    # print(nodes)

    how_many_towards = defaultdict(int)
    for p in P:
        how_many_towards[p] += 1

    # print(f'{how_many_towards=}')
    # print(f'{P=}')
    # print(f'{nodes=}')

    res = 0
    i = 0

    while i < len(nodes):
        # print(f'{i=}')

        relevant = nodes[i:i+how_many_towards[P[nodes[i]]]]
        # print(f'{relevant=}')

        if P[nodes[i]] == 0:
            return res + sum([F[r] for r in relevant])

        if how_many_towards[P[nodes[i]]] == 1:
            F[P[nodes[i]]] = max(F[nodes[i]], F[P[nodes[i]]])
            i += 1
            continue

        smallest = min([F[r] for r in relevant])
        res += sum([F[r] for r in relevant]) - smallest
        F[P[nodes[i]]] = max(smallest, F[P[nodes[i]]])
        i += len(relevant)

        # print(f'{F=}')
        # print(f'{res=}')
        # print('-' * 10)

    return 0
    # assert False


def go():
    t = input()
    inputs = []
    for _ in range(int(t)):
        row = []
        row.append(int(input()))
        row.append(list(map(int, input().split(' '))))
        row.append(list(map(int, input().split(' '))))
        inputs.append(row)

    for i, inputt in enumerate(inputs):
        res = get_best(*inputt)
        print(
            f'Case #{i+1}: {str(res)}'
        )


def main():
    go()


if __name__ == '__main__':
    main()