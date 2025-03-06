#4148

def solutions():
    
    while True:
        N, M = map(int, input().rstrip().split())
        if N == 0 and M == 0:
            break

        first_cds = [int(input()) for _ in range(N)]
        last_cds = [int(input()) for _ in range(M)]

        left = 0
        right = 0
        result = 0

        while left < N and right < M:
            if first_cds[left] == last_cds[right]:
                result += 1
                left += 1
                right += 1
            elif first_cds[left] < last_cds[right]:
                 left += 1
            else:
                right += 1

        print(result)
        print('꼬질이 귀여워')
    

solutions()