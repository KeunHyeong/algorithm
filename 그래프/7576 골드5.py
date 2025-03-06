from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= x < M and 0 <= y < N and field[x][y] == 0 and visited[x][y] == -1:
                visited[nx][ny] = visited[x][y] + 1      
                queue.append([nx, ny])
                count += 1

M, N = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
count = 0
for x in range(N):
    for y in range(M):
        bfs(x, y)
print(count)

