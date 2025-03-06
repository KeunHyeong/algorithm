#1855번

def solutions():
    n = int(input())

    crypto_str = str(input().rstrip())
    length = int(len(crypto_str) / n)
    arr = []

    for i in range(length):
        if i % 2 == 1:
            temp = crypto_str[i*n:(i+1)*n][::-1]
            arr.append(temp)
        else:
            arr.append(crypto_str[i*n:(i+1)*n])
    
    result = []
    for i in range(n):
        for j in range(len(arr)):
            result.append(arr[j][i])

    print(''.join(result))

solutions()