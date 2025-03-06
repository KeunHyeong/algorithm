s = input()
count = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count += 1

if count == 0:
    print(0)
else:
    print((count + 1) // 2)


s = input()  # 문자열로 받기
count = 0

# 구간 전환 횟수 세기
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count += 1

# 최소 뒤집기 횟수: 구간 수의 절반 (올림)
if count == 0:  # 모두 같은 숫자인 경우
    print(0)
else:
    print((count + 1) // 2)