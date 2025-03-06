#1942

def solutions():

    times = []
    for _ in range(3):
        front, last = input().split()
        times.append((front, last))


    result = []
    for front, last in times:
        front_h, front_m, front_s = map(int, front.split(":"))
        last_h, last_m, last_s = map(int, last.split(":"))

        front_seconds = front_h * 3600 + front_m * 60 + front_s
        last_seconds = last_h * 3600 + last_m * 60 + last_s

        count = 0
        if front_seconds > last_seconds:
            count += len([i for i in range(front_seconds, 86400) if i % 3 == 0])
            count += len([i for i in range(0, last_seconds + 1) if i % 3 == 0])
        else:
            count += len([i for i in range(front_seconds, last_seconds + 1) if i % 3 == 0])
        result.append(count)
    
    for item in result:
        print(item)
        
solutions()
    #     front = int(''.join(str(times[i*2]).split(":")))
    #     last = int(''.join(str(times[i*2+1]).split(":")))
        
    #     count = 0
    #     if front > last :
    #         count_front = 235959 - front

    #         for i in range(count_front):
    #             if i % 3 == 0:
    #                 count += 1

    #         for i in range(last, i-1):
    #             if i % 3 == 0:
    #                 count += 1
    #     else:
    #         dummy = last - front
    #         print(dummy)
    #         for i in range(dummy):
    #             if i % 3 == 0:
    #                 count += 1
    #     result.append(count)
    
    # print(result)








