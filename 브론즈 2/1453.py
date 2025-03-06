#1453

def solutions():
    N = int(input())
    input_arr = list(map(int, input().split()))

    dic = {}
    for i in range(N):
        if input_arr[i] in dic:
            dic[input_arr[i]] += 1
        else:
            dic[input_arr[i]] = 1

    result = []
    for _, value in dic.items():
        if value >= 2:
            result.append(value)

    print(sum(result) - len(result))

# solutions()

def solutions():
    N = int(input())
    seats = list(map(int, input().split()))

    occupieds_seats = set()
    rejected_count = 0

    for seat in seats:
        if seat in occupieds_seats:
            rejected_count += 1
        else:
            occupieds_seats.add(seat)
    print(rejected_count)

solutions()