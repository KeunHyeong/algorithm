# n = int(input())
# dp = [0] * (n+1)

# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1
#     print(dp[i], dp[i-1] + 1)

# n = int(input())
# dp = [0] * (n + 1)  # 0부터 n까지의 최소 횟수를 저장

# for i in range(2, n + 1):  # 2부터 n까지 계산
#     dp[i] = dp[i - 1] + 1  # 1 빼기 연산 먼저
#     if i % 2 == 0:         # 2로 나눠지면
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:         # 3으로 나눠지면
#         dp[i] = min(dp[i], dp[i // 3] + 1)

# print(dp[n])

n = int(input())

result = 0
for i in range(1, n+1):
    result += i
print(result)