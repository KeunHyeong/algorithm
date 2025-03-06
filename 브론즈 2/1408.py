#1408

def solutions():
    current_h,current_m,current_s = input().rstrip().split(":")
    mission_h,mission_m,mission_s = input().rstrip().split(":")

    current_time = int(current_h) * 3600 + int(current_m) * 60 + int(current_s)
    mission_time = int(mission_h) * 3600 + int(mission_m) * 60 + int(mission_s)

    remaining_time = (mission_time - current_time) % 86400

    print(change_digit(remaining_time))

def change_digit(time):
    hh = time//3600
    mm =  (time % 3600) // 60
    ss = time % 60
    return str(f"{hh:02}:{mm:02}:{ss:02}")
solutions()


from datetime import datetime, time
a = input()
b = input()
current_time = datetime.strptime(a,"%H:%M:%S")
mission_time = datetime.strptime(b,"%H:%M:%S")
default_time = datetime(1900,1,2,0,0,0)
if current_time > mission_time:
    timedelta
#     remaining_time = current_time - mission_time
#     print((default_time-remaining_time).time())
else:
    print(mission_time - current_time)

    from datetime import datetime, timedelta

# 입력 받기
a = input("Enter current time (HH:MM:SS): ")
b = input("Enter mission time (HH:MM:SS): ")

# 시간 파싱
current_time = datetime.strptime(a, "%H:%M:%S")
mission_time = datetime.strptime(b, "%H:%M:%S")

# 시간 차이 계산
if current_time > mission_time:
    # 다음 날로 넘어가는 경우
    remaining_time = timedelta(days=1) - (current_time - mission_time)
else:
    # 같은 날
    remaining_time = mission_time - current_time

# 결과 출력
print(str(remaining_time))
