def solutions():
    C, K = map(int, input().split())
    
    # 반올림할 단위 계산 (10^K)
    rounding_unit = 10 ** K

    # 반올림 계산
    rounded_price = round(C / rounding_unit) * rounding_unit

    # 결과 출력
    print(rounded_price)

solutions()