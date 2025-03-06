
# import sys
# sys.setrecursionlimit(100000)

# def dfs(x, y):
#     if x < 0 or x >= M or y < 0 or y >= N or field[x][y] == 0:
#         return
#     field[x][y] = 0
#     dfs(x-1, y)
#     dfs(x+1, y)
#     dfs(x, y-1)
#     dfs(x, y+1)

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())

#     field = [[0] * N for _ in range(M)]
    
#     for _ in range(K):
#         x, y = map(int, input().split())
#         field[x][y] = 1

#     count = 0
#     for i in range(M):
#         for j in range(N):
#             if field[i][j] == 1:
#                 dfs(i,j)
#                 count+=1
#     print(count)








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
                # visited.append((nx, ny))
                visited[nx][ny] = 1
                queue.append((nx, ny))

N = int(input())

for _ in range(N):
    M, N, K = map(int, input().split())

    field = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int , input().split())
        field[x][y] = 1
    
    count = 0
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    print(count)



























