#1259번

def solutions():
    while True:
        n  = input().strip()
        if n == '0':
            return
        arr = [i for i in n]

        if arr == arr[::-1]:
            print('yes')
        else:
            print('no')

solutions()