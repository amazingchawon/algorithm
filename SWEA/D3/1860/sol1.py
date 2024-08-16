# [D3] 1860 진기의 최고급 붕어빵

import sys
sys.stdin = open('input.txt', 'r')

def store(time, cnt):
    if customers[0] < M:  # 영업전에 오는 손님이 있다면
        return 'Impossible'

    idx = 0

    while time <= customers[-1]:
        if time % M == 0 and time != 0:     # 붕어빵이 완성되는 시간이면,
            cnt += K                        # 붕어빵 굽기

        while idx < len(customers):
            if time < customers[idx]:       # 현재 시간보다 늦게 오는 손님이라면
                break                       # 조건문 탈출

            if time == customers[idx]:      # 손님이 올 시간이고,
                if cnt <= 0:                 # 만들어진 붕어빵이 없으면,
                    return 'Impossible'
                else:                       # 만들어진 붕어빵이 있으면,
                    cnt -= 1                # 팔기
                idx += 1
        time += 1

    return 'Possible'

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())                 # N : 손님 수, M : 붕어빵 굽는데 걸리는 시간, K : 한 번에 만들 수 있는 붕어빵의 수
    customers = sorted(list(map(int, input().split()))) # 손님이 오는 시간을 담은 배열

    answer = store(0, 0)

    print(f'#{t} {answer}')

