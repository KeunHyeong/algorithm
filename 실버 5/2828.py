#2828

def solutions():
    N, M = map(int, input().split())
    J = int(input())
    apple_dropped_positions = [int(input()) for _ in range(J)]

    left = 1
    right = M
    total_distance = 0

    for position in apple_dropped_positions:
        if position < left:
            distance = left - position
            left -= distance
            right -= distance
            total_distance += distance
        elif position > right:
            distance = position - right
            left += distance
            right += distance
            total_distance += distance
            
    print(total_distance)

solutions()