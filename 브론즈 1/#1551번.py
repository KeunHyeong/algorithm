#1551번

def solutions():
    n, k = map(int, input().split())
    arr = list(map(int, input().split(',')))

    for _ in range(k):
        arr = [arr[i+1] - arr[i] for i in range(len(arr) -1)]

    print(','.join(map(str, arr)))

solutions()