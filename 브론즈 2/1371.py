#1371

def solutions():
    import sys
    input_arr = []
    for line in sys.stdin:
        input_arr.extend(line.strip())

    dic = {}
    for item in input_arr:
        if item != " ":
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
    
    mx = max(dic.values(), default=0)
    ch = ''

    result = []
    for item in dic.items():
        if mx == item[1]:
            result.append(item[0])
    result.sort()
    print(''.join(result))

solutions()

# def solutions():
#     import sys
#     input_arr = []
#     for line in sys.stdin:
#         input_arr.extend(line.strip())

#     dic = {}
#     for item in input_arr:
#         if item.isalpha():  # 알파벳만 처리
#             if item in dic:
#                 dic[item] += 1
#             else:
#                 dic[item] = 1

#     # 최대 빈도 찾기
#     mx = max(dic.values(), default=0)
    
#     # 최대 빈도를 가진 문자들 찾기
#     result = [key for key, value in dic.items() if value == mx]
#     result.sort()  # 사전순 정렬

#     print(''.join(result))

# solutions()
