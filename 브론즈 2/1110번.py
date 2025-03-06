#1110번

def solutions():
    input_arr = [list(input().strip()) for _ in range(8)]

#i짝수 일때 j도 짝수일때 판이 하얀색
    count = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if input_arr[i][j] == 'F':
                        count += 1
            else:
                if j % 2 == 1:
                    if input_arr[i][j] == 'F':
                        count += 1

    print(count)
solutions()
    

