#1189


def solutions():
    r,c,k = map(int, input().split())
    home_map = [list(input()) for _ in range(r)]

    start_x = home_map[0][0]
    start_y = home_map[r][0]

    for i in range(r):
        distance = 0
        for j in range(c):

            if home_map[start_x + i][start_y + j] != 'T':
                distance += 1
            
    print("")


solutions()