#6550

def solutions():
    import sys

    for line in sys.stdin:
        s, t = line.strip().split()
        if not line:
            break
        print(is_subsequence(s, t))

def is_subsequence(s, t):
    i, j = 0, 0
    while j < len(t):
        if i < len(s) and s[i] == t[j]:
            i+=1
        j += 1
    return "Yes" if i == len(s) else "No"
    
 

solutions()