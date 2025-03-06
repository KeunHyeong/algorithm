#1159번

def solutions():
    n = int(input())

    dic = {}
    input_arr = [list(input().split()) for i in range(n)]
    for i in range(n):
        if input_arr[i][0][0] in dic:
            dic[input_arr[i][0][0]] += 1
        else:
            dic[input_arr[i][0][0]] = 1

    result = []
    for j in dic:
        if j[1] >= 5:
            result.append(j[0])

    if len(result) > 0:
        result = sorted(result)
        print(''.join(result))
    else:
        print("PREDAJA")

solutions()