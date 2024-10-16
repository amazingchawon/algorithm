# [LV2] 92341 주차 요금 계산

def solution(fees, records):
    answer = []

    # STEP 1. 데이터 받기

    # 기본 시간, 기본 요금, 단위시간, 단위요금
    grace_period, default, time_unit, fee = fees

    # cars dict -> 차량번호 : [(시, 분), (시, 분), ..] 형태로 저장
    cars = {}
    for record in records:
        # 띄어쓰기 기준으로 list 생성
        data = record.split(' ')
        # '05:34' -> '05', '34'로 변경
        H, M = data[0].split(':')
        H, M = int(H), int(M)
        if data[1] in cars:
            cars[data[1]].append((H, M))
        else:
            cars[data[1]] = [(H, M)]

    # STEP 2. 주차 요금 계산
    for num, times in cars.items():
        # times는 이미 정렬된 상태
        # times의 길이가 홀수라면, 23:59분에 출차한 기록 더해주기
        if len(times) % 2 == 1:
            times.append((23, 59))

        # 주차 요금 계산
        time_total = 0
        cost = default
        for idx in range(0, len(times), 2):
            start_hour, start_min = times[idx]
            end_hour, end_min = times[idx + 1]
            time_total += (end_hour - start_hour) * 60 + (end_min - start_min)

        if time_total > grace_period:
            time = (time_total - grace_period)
            # 주차한 시간이 단위시간으로 나누어 떨어지지 않으면 1분 추가
            if time % time_unit != 0:
                time = (time // time_unit) + 1
            else:
                time //= time_unit
        else:
            time = 0

        # cost 갱신
        cost += time * fee

        cars[num] = cost

    # STEP 3. 번호가 작은 순서대로 answer에 추가
    tmp = sorted(cars.items())
    for num, cost in tmp:
        answer.append(cost)

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))