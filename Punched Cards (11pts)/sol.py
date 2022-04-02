def printColumn(c: int, r: int):
    string = '+-' if r % 2 == 0 else '|.'

    print(string*c + string[0])


for i in range(int(input())):
    r, c = map(int, input().split())

    print(f'Case #{i+1}:')

    for cr in [0, 1]:
        print('..', end='')
        printColumn(c-1, cr)

    for cr in range(2, r*2+1):
        printColumn(c, cr)
