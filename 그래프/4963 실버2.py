
def dfs(x, y, field, visited, w, h):
    visited[x][y] = 1

    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and field[nx][ny] == 1:
            dfs(nx, ny, field, visited, w, h)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    if w == 1 and h == 1:
        field = [list(map(int, input().split()))]
    else:   
        field = [list(map(int,input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if field[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, field, visited, w, h)
                count += 1
    print(count)

