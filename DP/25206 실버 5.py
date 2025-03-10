dic = {"A+":4.5, "A0":4.0, "B+":3.5,
       "B0":3.0, "C+":2.5, "C0":2.0,
       "D+":1.5, "D0":1.0, "F":0.0 }

a = []
b = []
for _ in range(20):
    _, h, d = input().split()
    a.append(float(h))
    b.append(d)

total = 0.0
total_credits = 0.0
for i in range(20):
    if b[i] != "P":
        total += a[i] * dic[b[i]]
        total_credits += a[i]

print("{:.6f}".format(total/total_credits))
