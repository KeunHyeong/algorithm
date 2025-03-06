#5635

def solutions():
    N = int(input())
    lst = [(input().split()) for _ in range(N)]

    for _ in range(N):
        try :
            name, d, m, y = input().rstrip().split()
            lst.append(int(y), int(m), int(d), name)
        except:
            print("value input exception")
            return

    lst.sort()

    print(lst[-1][3])
    print(lst[0][3])


solutions()