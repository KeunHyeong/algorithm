#1431번

def solutions():
    n = int(input())
    serial_nums = [input().strip() for _ in range(n)]

    def digit_sum(s: str) -> int:
        return sum(int(ch) for ch in s if ch.isdigit())
    
    serial_nums.sort(key=lambda s: (len(s), digit_sum(s), s))

    for s in serial_nums:
        print(s)

solutions()