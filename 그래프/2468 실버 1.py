from collections import deque, defaultdict

def bfs(x, y,visited, field, h):
    queue = deque([(x, y)])
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and field[nx][ny] > h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

max_height = max(max(row) for row in field)

max_safe_areas = 0
for h in range(N, max_height + 1):
    visited = [[0] *  N for _ in range(N)]
    safe_areas = 0

    for i in range(N):
        for j in range(N):
            if field[i][j] > h and visited[i][j] == 0:
                bfs(i, j, visited, field, N)
                safe_areas += 1
    max_safe_areas = max(max_safe_areas, safe_areas)
print(max_safe_areas)







from collections import deque

def bfs(x, y, h, visited, field, N):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    # 상하좌우 이동
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고, 방문하지 않았으며, 높이가 h보다 큰 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] > h:
                visited[nx][ny] = 1
                queue.append((nx, ny))

# 입력 받기
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 구하기 (비의 양 범위 설정용)
max_height = max(max(row) for row in field)

# 안전 영역 최대 개수 계산
max_safe_areas = 0
for h in range(N, max_height + 1):  # 비의 양: 0부터 최대 높이까지
    visited = [[0] * N for _ in range(N)]
    safe_areas = 0
    
    # 모든 좌표 탐색
    for i in range(N):
        for j in range(N):
            if field[i][j] > h and not visited[i][j]:  # 물에 잠기지 않았고 방문 안 한 경우
                bfs(i, j, h, visited, field, N)
                safe_areas += 1
    
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)