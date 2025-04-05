n = int(input())
lst = [int(input()) for _  in range(n)]

if n == 1:
    print(0)
else:
    dasom = lst[0]
    other = sorted(lst[1:], reverse=True)
    count = 0
    while dasom <= other[0]:
        other[0] -= 1
        dasom += 1
        count += 1
        other.sort(reverse=True)
    print(count)
