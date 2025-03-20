N,A = int(input()),list(map(int, input().split()))

DP = [1 for i in range(N)]

print(DP)
for i in range(1, N):
    print()
    for j in range(i):
        print(j, end=" ")
        if A[i] > A[j]:
            DP[i] = max(DP[i],DP[j]+1)

print(max(DP))