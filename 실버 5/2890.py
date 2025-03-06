def solutions():
    R, C = map(int, input().split())

    # 각 팀의 카약 위치 기록 (key: 팀 번호, value: 결승선으로부터의 거리)
    distance = {}

    for _ in range(R):
        row = input().strip()
        if 'F' in row:
            finish_line = row.index('F')  # 정확한 결승선 위치 찾기
        for i in range(len(row)):
            if row[i] in '123456789':  # 카약 발견
                team = row[i]
                dist = finish_line - (i + 2)  # 결승선으로부터의 거리 계산
                distance[team] = dist
                break  # 한 줄에 하나의 카약만 존재

    # 거리 기준으로 순위 계산
    sorted_distance = sorted(distance.items(), key=lambda x: x[1])  # 거리 기준 오름차순 정렬
    rank = {}
    current_rank = 1
    prev_dist = -1

    for idx, (team, dist) in enumerate(sorted_distance):
        if dist != prev_dist:  # 이전 거리와 다르면 순위 증가
            current_rank = idx + 1
        rank[team] = current_rank
        prev_dist = dist

    # 1번부터 9번 팀까지의 등수 출력
    for i in range(1, 10):
        print(rank[str(i)])

solutions()
