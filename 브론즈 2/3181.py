def solutions():
    words = input().split()
    distincts = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

    result = [words[0][0].upper()]

    for i in range(1, len(words)):
        if words[i] not in distincts:
            result.append(words[i][0].upper())

    print(''.join(result))

solutions()
