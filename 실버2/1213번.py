#1213번

def solve():
    import sys
    name = sys.stdin.readline().rstrip()

    from collections import Counter
    counts = Counter(name)

    odd_counter = [ch for ch, cnt in counts.items() if cnt % 2 == 1]

    #홀수 일때는 1만 되고 짝수일때는 0만 된다

    #짝수
    if len(name) % 2 == 0:
        if len(odd_counter) != 0:
            print("I'm Sorry Hansoo")
            return
    else:
        if len(odd_counter) != 1:
            print("I'm Sorry Hansoo")
            return

    front = []
    middle_ch = ''

    for ch in sorted(counts.keys()):
        cnt = counts[ch]
        if cnt % 2 == 1:
            middle_ch = ch
        front.extend(ch *(cnt // 2))

    front = ''.join(front)
    behind = front[::-1]
    print(front + middle_ch + behind)
    
solve()