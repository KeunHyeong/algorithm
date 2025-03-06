#2857

def solutions():
    input_arr = [input().rstrip() for _ in range(5)]
    
    isExistFBI = False
    for i in range(5):
        if "FBI" in input_arr[i]:
            print(i+1, end=" ")
            isExistFBI = True
        
        if i == 4 and not isExistFBI:
            print("HE GOT AWAY!")


solutions()