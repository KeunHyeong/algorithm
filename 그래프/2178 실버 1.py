# from collections import deque

# def bfs(x, y):
#     queue = deque([(x, y)])
#     visited[x][y] = 1

#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 1 and visited[nx][ny] == -1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append((nx, ny))
                
#     return visited[N-1][M-1]

# N, M = map(int, input().split())
# field = [list(map(int, input())) for _ in range(N)]
# visited = [[-1] * M for _ in range(N)]

# result = bfs(0,0)
# print(result)






from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and field[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    print()
    for i in range(N):
        for j in range(M):
            print(visited[i][j], end=" ")
        print("\n", end="")

    return visited[N-1][M-1]

N, M = map(int, input().split())
field = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = bfs(0,0)
# print(result)
