from collections import deque, defaultdict

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(sorted(graph[vertex], reverse=True))
        
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(sorted(graph[vertex]))

    return visited

def main():
    n,m,v = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(' '.join(map(str, dfs(graph, v))))
    print(' '.join(map(str, bfs(graph, v))))

if __name__ == "__main__":
    main()


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(sorted(graph[vertex]), reversed = True)

    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.append(sorted(graph[vertex]))
    return visited
