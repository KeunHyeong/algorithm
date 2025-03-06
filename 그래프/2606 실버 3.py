
from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
            print(queue)

    return len(visited) - 1
            

N = int(input())
pair = int(input())

graph = defaultdict(list)
for  _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = bfs(graph, 1)
print(result)


