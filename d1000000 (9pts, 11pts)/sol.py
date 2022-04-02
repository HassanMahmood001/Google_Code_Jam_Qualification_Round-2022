
for t in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)

    for i, v in enumerate(arr):
        if v < n - i:
            arr = arr[:v+i-n]  # -(n-i-v)
            n = v+i  # n - (n-i-v)

    print(f'Case #{t+1}: {len(arr)}')
