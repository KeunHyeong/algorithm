#5671


def valid_check(room):
    room = str(room)
    return len(room) == len(set(room))

def count_valid_rooms(N, M):
    count = 0
    for room in range(N, M+1):
        if valid_check(room):
            count += 1
    return count

def solutions():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        N, M = map(int, line.split())
        print(count_valid_rooms(N, M))

solutions()