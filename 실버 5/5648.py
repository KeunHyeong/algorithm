
def solutions():
    import sys
    result = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break

        for item in line.split():
            try:
                reversed_num = int(item[::-1])
                result.append(reversed_num)
            except ValueError:
                print("error")

    result.sort()
    for item in result:
        print(item)


solutions()