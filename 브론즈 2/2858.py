#2858

from itertools import product

def solutions():
    L, W = map(int, input().split())

    LW = L+W
    make_data = []
    for i in range(1, LW):
        if LW % i == 0:
            make_data.append(i)

    result = []
    for f,l in product(make_data, repeat=2):
        if f * l == LW:
            if f - l <= 2 and f - l >= 0:
                result.append((f, l))

    print(result[0][0], result[0][1])

solutions()