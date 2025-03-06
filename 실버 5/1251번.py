# 1251번

def find_lexicographically_smallest():
    inputStr = input()
    n = len(inputStr)
    smallest = None

    for i in range(1, n-1):
        for j in range(i+1, n):
            first = inputStr[:i][::-1]
            mid = inputStr[i:j][::-1]
            last = inputStr[j:][::-1]

            sumStr = first + mid + last

            if smallest is None or sumStr < smallest:
                smallest = sumStr
                
    print(smallest) #input: mobitel
find_lexicographically_smallest()




