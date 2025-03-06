#1592

def solutions():
    #던지는 횟수, 끝나는 횟수, 번째 있는 사람에게 던진다
    N,M,L = map(int, input().split())

    received = N * [0]

    current_position = 0
    throws = 0

    while True:
        received[current_position] += 1

        if received[current_position] == M:
            break

        throws += 1

        if received[current_position] % 2 == 1:
            current_position = (current_position + L) % N
        else:
            current_position = (current_position - L) % N
    print(throws)




solutions()