#1673

def solutions():
    while True:
        try:
            #쿠폰, 도장
            N,K = map(int, input().split())
            stamp = N
            total_chicken = N 

            while stamp >= K:
                addtional_chicken = stamp // K
                total_chicken += addtional_chicken
                stamp = stamp % K + addtional_chicken

            print(total_chicken)

        except:
            break

solutions()