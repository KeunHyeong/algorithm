#2822

def solutions():
    problems = [(int(input()),i+1) for i in range(8)]
    problems.sort(reverse=True)

    count_nums = []
    problems_sum = 0

    for i in range(5):
        problems_sum += problems[i][0]
        count_nums.append(problems[i][1])

    print(problems_sum)
    count_nums.sort()
    print(' '.join(map(str, count_nums)))

solutions()