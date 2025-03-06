#1292번

def solutions():
    a, b = map(int,input().split())
    arr = []

    num = 1

    while len(arr) < b:
        for _ in range(num):
            arr.append(num)
        num += 1

    print(sum(arr[a-1:b]))
    
solutions()