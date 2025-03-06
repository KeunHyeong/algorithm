from decimal import Decimal
dic ={'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
      'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
      'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
      'D+': 1.3, 'D0': 1.0, 'D-': 0.7}

N = int(input())
records = [input().split() for _ in range(N)]

#과목명, 학점, 성적
result = 0
points = 0.0
for _, point, prize in records:
    points += float(point)
    result += dic[prize] * float(point)

print(round(Decimal(str(result/points)), 2))
