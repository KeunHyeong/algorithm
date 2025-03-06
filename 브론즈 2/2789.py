#2789

def solutions():
    words = input().rstrip()
    cambridge = "CAMBRIDGE"

    result = []
    for word in words:
        if word not in cambridge:
            result.append(word)
    
    print(''.join(result))       

solutions()