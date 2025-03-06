def makeBoss():
    n = int(input())
    arr = {}

    for i in range(n):
        m = list(map(int, input().split()))
        arr[i] = m
    
    total_shared = [0] * n

    for i in range(n):
        for k in range(n):
            if i != k:
                for j in range(5):
                    if arr[i][j] == arr[k][j]:
                        total_shared[i] += 1
                        break

    mx = max(total_shared)
    for i in range(n):
        if total_shared[i] == mx:
            print(i+1)
            break

makeBoss()

def makeBoss():
    n = int(input("학생 수를 입력하세요: "))
    arr = {}

    # 학생별 반 정보를 입력받아 arr에 저장
    for i in range(n):
        m = list(map(int, input(f"{i+1}번 학생의 반 정보를 입력하세요: ").split()))
        arr[i] = m

    # 같은 반이었던 학생 수를 저장할 리스트
    total_shared = [0] * n

    # 모든 학생 간의 반 정보 비교
    for i in range(n):
        for k in range(n):
            if i != k:  # 자기 자신은 비교하지 않음
                for j in range(5):  # 1학년부터 5학년까지 비교
                    if arr[i][j] == arr[k][j]:
                        total_shared[i] += 1
                        break  # 한 학년에서 같은 반이면 더 이상 비교하지 않음

    # 최댓값을 가진 학생 번호 찾기
    max_shared = max(total_shared)
    for i in range(n):
        if total_shared[i] == max_shared:
            print(i + 1)  # 학생 번호는 1부터 시작
            break
