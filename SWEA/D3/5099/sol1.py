# [D3] 5099 피자 굽기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))

    oven = pizzas[0:N]                      # 화덕에 피자 넣어주기
    pizzas_in_oven = [i for i in range(N)]  # 현재 오븐에 있는 피자 번
    idx = N                                 # pizzas 인덱스로 활용할 변수

    while idx < M:                          # 주어진 피자를 다 넣을 때까지 반복
        for i in range(N):
            oven[i] //= 2                   # 치즈 녹여주기
            if oven[i] == 0:                # 치즈가 다 녹았다면, 피자를 빼고
                oven[i] = pizzas[idx]       # 오븐에 생긴 빈자리에 새로운 피자 넣어주기
                pizzas_in_oven[i] = idx     # 현재 i번 위치에 있는 피자 이름 기록
                idx += 1
            if idx == M:
                break

    # [1, 2, 7, 6]의 경우 6이 나와야함 -> max(oven)으로 구현하면 7이 나옴
    # [1, 2, 7, 7]의 경우 뒤에 있는 피자가 나와야함 -> max(oven)으로 구현하면 앞에 7이 나옴
    max_cheese = max(oven)
    while oven.count(max_cheese) > 1:
        oven.pop(oven.index(max_cheese))
        pizzas_in_oven.pop(oven.index(max_cheese))
    answer = pizzas_in_oven[oven.index(max_cheese)] + 1
    if max_cheese % 2 == 1:
        for i in range(max_cheese+1, len(oven)):
            if oven[i] == max_cheese -1:
                answer = pizzas_in_oven[i] + 1

    # # max(oven) : 현재 오븐에 들어있는 피자 중에 제일 치즈가 많은 피자 찾기 -> 제일 늦게 녹을테니까
    # # oven.index : 그 피자가 들어있는 위치 찾기
    # # pizzas_in_oven[] : 피자 번호가 들어있는 리스트에서 번호 찾기
    # # + 1 : 인덱스라 번호로 출력하기 위해서 1 더해주기
    # answer = pizzas_in_oven[oven.index(max(oven))] + 1
    print(f'#{t} {answer}')