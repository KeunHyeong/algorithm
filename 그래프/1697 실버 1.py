from collections import deque, defaultdict

def bfs(N, K):
    MAX = 100001
    visited = [-1] * MAX
    queue = deque([N])
    visited[N] = 0

    while queue:
        x = queue.popleft()

        if x == K:
            return visited[x]
        
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return visited[K]


N, K = map(int, input().split())
print(bfs(N, K))

