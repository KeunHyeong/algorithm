n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse = True)

result = 0
for i in range(n):
    result += (list_a[i] * list_b[i])
print(result)