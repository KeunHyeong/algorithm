def solutions():
    A, B = input().split()

    min_A = str(A).replace('6', '5')
    min_B = str(B).replace('6', '5')

    max_A = str(A).replace('5', '6')
    max_B = str(B).replace('5', '6')

    print(int(min_A) + int(min_B), int(max_A) + int(max_B))

solutions()