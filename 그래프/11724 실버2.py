from collections import deque, defaultdict

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

N, M = map(int, input().split())
graph = defaultdict(list)
visited = set()
cc = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# result = bfs(graph, cc[0])

for vertex in range(1, N + 1):
    if vertex not in visited:
        bfs(graph, vertex, visited)
        cc += 1
print(cc)




