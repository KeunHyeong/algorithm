
a, b = map(int, input().split())

current = b
count = 1
while current > a:
    if current % 2 == 0:
        current //= 2
    elif current % 10 == 1:
        current = (current - 1)//10
    else:
        count = -1
        break
    count += 1

if current == a:
    print(count)
else:
    print(-1)




    