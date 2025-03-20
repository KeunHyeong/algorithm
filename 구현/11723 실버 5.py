# 실패
import sys
m = int(input())
s = set()

for _ in range(m):
    command = input().rstrip()

    if command == 'all':
        s = [i for i in range(1, 21)]
    elif command == "empty":
        s = []
    else:
        op, x = command.split()
        if op == 'add':
            if x not in s:
                s.add(x)
        elif op == 'remove':
            if x in s:
                s.discard(x)
        elif op == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)
            


    


