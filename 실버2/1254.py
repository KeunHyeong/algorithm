# #1254

# def solutions():
#     input_str = str(input())

#     if input_str == input_str[::-1]:
#         return print(len(input_str))
    
#     for char in input_str[::-1]:
#         if input_str != input_str[::-1]:
#             if input_str[-1] != char:
#                 input_str += char
#         else:
#             break
#     print(len(input_str), input_str)


# solutions()

def solutions():
    input_str = input()
    if input_str == input_str[::-1]:
        print(len(input_str))
        return
    
    for i in range(len(input_str)):
        temp = input_str + input_str[:i][::-1]
        if temp == temp[::-1]:
            print(len(temp))
            break

solutions()