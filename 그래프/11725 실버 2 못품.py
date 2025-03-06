from collections import deque, defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

print(graph)