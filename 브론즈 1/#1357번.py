#1357번

def solutions():
    x, y = list(map(str, input().split()))
    
    reversedX = ''
    reversedY = ''

    for i in reversed(range(len(x))):
        reversedX += x[i]

    for j in reversed(range(len(y))):
        reversedY += y[j]
    
    reversedXY = int(reversedX) + int(reversedY)
    reversedXY = str(reversedXY)
    result = ''

    for k in reversed(range(len(reversedXY))):
        result += reversedXY[k]
        
    print(int(result))

solutions()

#개선된 코드
def solution():
    x, y = input().split()
    
    # 숫자를 뒤집고 더한 후 다시 뒤집음
    reversed_sum = int(str(int(x[::-1]) + int(y[::-1]))[::-1])
    
    print(reversed_sum)

solution()