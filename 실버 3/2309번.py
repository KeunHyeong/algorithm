# def solutions():
#     # 아홉 명의 난쟁이 키를 입력받습니다.
#     heights = [int(input()) for _ in range(9)]
    
#     total_sum = sum(heights)  # 전체 키의 합을 구합니다.
#     target_sum = total_sum - 100  # 일곱 명의 난쟁이 합이 100이 되어야 하므로, 두 명의 키 합은 target_sum이어야 합니다.
    
#     # 두 명의 키 합이 target_sum이 되는 경우를 찾습니다.
#     for i in range(8):
#         for j in range(i + 1, 9):
#             if heights[i] + heights[j] == target_sum:
#                 # 이 두 명을 제외한 나머지 일곱 명을 구합니다.
#                 result = [heights[k] for k in range(9) if k != i and k != j]
#                 result.sort()  # 일곱 명의 키를 오름차순으로 정렬합니다.
#                 print(*result)  # 결과를 출력합니다.
#                 return

# solutions()

def solutions():
    heights = [int(input()) for _ in range(9)]

    total_sum = sum(heights)
    target_sum = total_sum - 100

    for i in range(8):
        for j in range(i+1, 9):
            if heights[i] + heights[j] == target_sum:
                result = [heights[k] for k in range(9) if k != i and k != j]
                result.sort()
    
    for item in result:
        print(item)

solutions()