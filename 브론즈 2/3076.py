def create_chessboard(R, C, A, B):
    # 기본 체스판 패턴 생성
    base_board = []
    for i in range(R):
        row = []
        for j in range(C):
            if (i + j) % 2 == 0:
                row.append('X')
            else:
                row.append('.')
        base_board.append(row)

    # 확장된 체스판 생성
    expanded_board = []
    for row in base_board:
        # 각 열을 B번 반복
        expanded_row = ''.join(cell * B for cell in row)
        # 각 행을 A번 복제
        for _ in range(A):
            expanded_board.append(expanded_row)

    # 출력
    for line in expanded_board:
        print(line)

# 입력 받기
R, C = map(int, input().split())
A, B = map(int, input().split())

create_chessboard(R, C, A, B)
