n = list(input())
n.sort(reverse= True)

if sum(map(int, n)) % 3 != 0:
    print(-1)
elif n[-1] != '0':
    print(-1)
else:
    print(*n, sep='')
