
for t in range(int(input())):
    cmyk = list(map(min, zip(*[map(int, input().split()) for _ in range(3)])))

    result = []
    total = 1000000
    if sum(cmyk) < total:
        result.append('IMPOSSIBLE')
    else:
        for i in cmyk:
            result.append(f'{min(total, i)}')
            total -= min(total, i)

    print(f'Case #{t+1}:', *result)
