def solve():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    # 각 행을 문자열로 입력받음
    grid = [input().strip() for _ in range(N)]

    max_area = 1  # 최소 1x1 정사각형은 항상 가능

    # 모든 행(r), 모든 열(c)에 대해 탐색
    for r in range(N):
        for c in range(M):
            # 한 변이 몇 칸짜리인지 = side
            # 실제로 반복문에서는 side가 아니라 (side-1)을 'k'로 다루는 경우가 많음
            # k의 최댓값: min(N-1-r, M-1-c)
            max_k = min(N - 1 - r, M - 1 - c)
            for k in range(max_k + 1):
                # 꼭짓점 4개
                top_left  = grid[r][c]
                top_right = grid[r][c + k]
                bottom_left  = grid[r + k][c]
                bottom_right = grid[r + k][c + k]

                # 모두 같은지 확인
                if top_left == top_right == bottom_left == bottom_right:
                    # 정사각형 변 길이 = k + 1
                    side = k + 1
                    area = side * side
                    if area > max_area:
                        max_area = area

    print(max_area)
solve()