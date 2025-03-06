#2526번

def solutions():
    N, P = map(int, input().split())
    sequence = []
    seen = {}
    
    current = N

    while current not in seen:
        seen[current] = len(sequence)
        sequence.append(current)
        current = (current * N) % P
    
    start_index = seen[current]
    cycle_length = len(sequence) - start_index
    print(cycle_length)
        
solutions()


# # N과 P를 입력받습니다.
# def find_cycle_length(N, P):
#     # 값을 저장할 리스트와 확인을 위한 딕셔너리 초기화
#     sequence = []
#     seen = {}

#     # 현재 값 초기화
#     current = N

#     while current not in seen:
#         # 현재 값을 딕셔너리에 저장하여 인덱스 기록
#         seen[current] = len(sequence)
#         # 시퀀스에 현재 값 추가
#         sequence.append(current)
#         # 다음 값 계산
#         current = (current * N) % P

#     # 반복이 시작되는 인덱스 찾기
#     start_index = seen[current]

#     # 반복되는 부분의 길이 계산
#     cycle_length = len(sequence) - start_index

#     return cycle_length

# # 테스트용 입력
# if __name__ == "__main__":
#     # 입력을 직접 받을 수 없는 환경에서는 아래와 같이 값을 설정
#     test_cases = [
#         (67, 31),  # Expected output: 3
#         (9, 3),    # Expected output: 1
#         (10, 6),   # Expected output: 1
#         (7, 11),   # Expected output: 10
#     ]

#     for N, P in test_cases:
#         print(f"N={N}, P={P} -> Cycle Length: {find_cycle_length(N, P)}")
