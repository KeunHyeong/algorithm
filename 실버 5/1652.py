def find_sleeping_spots():
    N = int(input())
    room = [input().strip() for i in range(N)]

    horizontal = 0  # 가로로 누울 자리 개수
    vertical = 0    # 세로로 누울 자리 개수

    # 가로로 누울 자리 찾기
    for row in room:
        count = 0
        for cell in row:
            if cell == '.':
                count += 1
            else:
                if count >= 2:  # 2칸 이상 빈칸이면 자리로 카운트
                    horizontal += 1
                count = 0
        if count >= 2:  # 행의 끝까지 빈칸인 경우 처리
            horizontal += 1

    # 세로로 누울 자리 찾기
    for col in range(N):
        count = 0
        for row in range(N):
            if room[row][col] == '.':
                count += 1
            else:
                if count >= 2:  # 2칸 이상 빈칸이면 자리로 카운트
                    vertical += 1
                count = 0
        if count >= 2:  # 열의 끝까지 빈칸인 경우 처리
            vertical += 1

    print(horizontal, vertical)

find_sleeping_spots()
