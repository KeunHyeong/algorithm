#실패
nums = input()
count = [0 for _ in range(10)]

for i in nums:
    count[int(i)] += 1

six_nine = (count[6] + count[9] + 1)//2
count[6] = six_nine
count[9] = 0

print(max(count))


888888