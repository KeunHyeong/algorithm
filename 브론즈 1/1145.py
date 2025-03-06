#1145

def solutions():
    nums = list(map(int, input().split()))

    i = min(nums)
    while True:
        count = 0
        for num in nums:
            if i % num == 0:
                count +=1
        if count >= 3:
            break
        i += 1

    print(i)

solutions()