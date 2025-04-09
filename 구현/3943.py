n = int(input())
lst = [int(input()) for _ in range(n)]
for i in lst:
    mx = i
    while True:
        if i == 1:
            break
        if i % 2 == 1:
            i = i * 3 + 1
        else:
            i = i / 2
        mx = max(mx, i)
    print(int(mx))