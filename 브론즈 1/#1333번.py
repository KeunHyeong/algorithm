#1356번

def solution():
    n = str(input())
    arr = [int(i) for i in n]

    for i in range(1, len(arr)):
        first_num = 1
        second_num = 1

        for j in arr[:i]:
            first_num *= j
        
        for z in arr[i:]:
            second_num *= z
        
        if first_num == second_num:
            print('YES')
            return
    print('NO')

solution()