#1773

def solutions():
    N, C = map(int, input().split())
    dic = {}
    for i in range(N):
        n = int(input())
        dic[i] = n
    
    result = {}
    for key, value in dic.items():
        for j in range(1, C + 1):
            if j % value == 0:
                result[j] = 1

    print(sum(result.values()))

solutions()

def solutions():
    N, C = map(int, input().split())
    dic = []
    for i in range(N):
        n = int(input())
        dic.append(n)
    
    result = set()
    for value in dic:
        for j in range(1, C + 1):
            if j % value == 0:
                result.add(j)

    print(len(result))

solutions()