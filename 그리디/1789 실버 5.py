n = int(input())

s = 0

count = 0
for i in range(1, n+1):
    if s > n:
        break  
    s += i
    count += 1
    print(count)
  
print(count)