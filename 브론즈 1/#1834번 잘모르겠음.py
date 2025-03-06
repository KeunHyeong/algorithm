#1834번 잘모르겠음

def solutions():
    n = int(input())




solutions()

def find_sum(N):
    result = 0
    for q in range(1, N + 1):
        result += q * (N + 1)
    print(result)

# 입력
N = int(input())
find_sum(N)


def find_sum(N):
    result = N * (N + 1) * (N + 1) // 2
    print(result)

# 입력
N = int(input())
find_sum(N)