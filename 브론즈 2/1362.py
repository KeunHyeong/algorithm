#1362

def solutions():
    input_arr = []
    while True:
        #적정 체중, 실제 체중
        val = input().split()
        input_arr.append(val)
        if val[0] == '0' and val[1] == '0':
            break

    result = []
    default_o = 0
    default_w = 0
    for item in input_arr:
        if item[0].isdigit() and item[1].isdigit():
            default_o = int(item[0])
            default_w = int(item[1])
            int_w = default_w
        else:
            o = item[0]
            if o == 'F':
                int_w += int(item[1])
            elif o == 'E':
                int_w -= int(item[1])
            elif o == '#':
                if int_w > (default_o/2) and int_w < (default_o * 2):
                    result.append(':-)')
                elif int_w <= 0:
                    result.append('RIP')
                else:
                    result.append(':-(')
    for i in range(len(result)):
        print(i+1, " ",result[i])

solutions()

def pet_game():
    scenario_number = 1  # 시나리오 번호
    while True:
        # 적정 체중(o)와 실제 체중(w) 입력
        o, w = map(int, input().split())
        if o == 0 and w == 0:  # 종료 조건
            break
        
        is_dead = False  # 펫이 사망했는지 여부
        while True:
            command = input().split()
            action = command[0]
            if action == "#":  # 현재 시나리오 종료
                break
            
            value = int(command[1])
            if not is_dead:  # 펫이 살아있을 때만 작용 처리
                if action == "F":
                    w += value  # 먹이를 준 경우
                elif action == "E":
                    w -= value  # 운동을 시킨 경우
                
                if w <= 0:  # 체중이 0 이하이면 펫 사망
                    is_dead = True

        # 결과 출력
        if is_dead:
            print(f"{scenario_number} RIP")
        elif o / 2 < w < o * 2:
            print(f"{scenario_number} :-)")
        else:
            print(f"{scenario_number} :-(")

        scenario_number += 1  # 다음 시나리오 번호

# 실행
pet_game()
