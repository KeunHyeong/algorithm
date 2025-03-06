#2546번
import sys
from collections import Counter

def solutions():
    N = int(input())
    input_str = sys.stdin.readline()
    input_arr = []

    for i in range(int(len(input_str)/6)):
        input_arr.append(input_str[i*6:(i+1)*6])

    dic = {'A':'000000', 'B':'001111', 'C':'010011',
           'D':'011100', 'E':'100110', 'F':'101001',
           'G':'110101', 'H':'111010'}
    
    count = Counter(input_arr)

    wrong_num = []
    print(input_arr)
    for item in input_arr:
        if item not in dic.values():
            wrong_num.append(item)


    print(wrong_num)


solutions()