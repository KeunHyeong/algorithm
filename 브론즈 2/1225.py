#1225

def solutions():
    A, B = map(str, input().split())

    total_sum = 0

    for i in A:
        for j in B:
            total_sum += int(i) * int(j)
    print(total_sum)

solutions()

# def solutions():
#     A, B = map(str, input().split())

#     # 각 자리 숫자를 곱하고 합을 계산
#     total_sum = 0
#     for i in A:
#         for j in B:
#             total_sum += int(i) * int(j)
#     print(total_sum)

# solutions()
