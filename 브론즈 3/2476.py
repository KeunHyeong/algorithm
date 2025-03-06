#2476

def solutions():
    from collections import Counter
    N = int(input())
    dices = []
    for _ in range(N):
        first, second, third = map(int, input().split())
        dices.append((first, second, third))

    result = []
    for first, second, third in dices:
        prize = 0
        if first == second and second == third:
            prize = first * 1000 + 10000
        elif first != second and second != third and first != third:
            prize = max([first, second, third], default=0) * 100
        else:
            count = Counter([first, second, third])
            mx = 0
            same_dice = 0
            for key, value in count.items():
                if mx < value:
                    mx = value
                    same_dice = key

            prize = same_dice*100 + 1000

        result.append(prize)
    print(max(result, default=0))
    

solutions()

    
