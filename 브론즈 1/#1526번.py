#1526번
from collections import deque

def solutions():
    n = int(input().strip())
    answer = 0

    queue = deque([4,7])

    while queue:
        num = queue.popleft()
        if num <= n:
            answer = max(answer, num)

            queue.append(num * 10 + 4)
            queue.append(num * 10 + 7)
            
    print(answer)

solutions()