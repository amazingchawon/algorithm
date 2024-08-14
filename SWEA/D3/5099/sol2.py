# [D3] 5099 피자 굽기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    pizzas = list(map(int, input().split()))
    pizza_num = 1

    # 오븐 채우기
    oven = [0] * N
    for i in range(N):
        tmp = [pizza_num, pizzas[pizza_num-1]]  # [피자 번호, 피자 치즈양]
        oven[i] = tmp                           # oven에 굽기
        pizza_num += 1                          # 피자 넘버 증가

    while oven.count(None) != N-1:      # 오븐에 1개의 피자가 남을때까지 반복
        for i in range(N):              # 오븐 순회
            if oven[i] == None:         # i번째 오븐이 비어있다면,
                continue                # 다음 오븐으로 넘어가기

            oven[i][1] //= 2                                    # 현재 피자 녹여주기
            if oven[i][1] == 0:                                 # 치즈가 다 녹았다면,
                if pizza_num > M:                               # 더 이상 구워야할 피자가 없다면,
                    oven[i] = None                              # 오븐 비워주기
                    if oven.count(None) == N-1:                 # 오븐에 1개의 피자만 남았다면,
                        break
                else:                                           # 구울 피자가 남아있으면
                    oven[i] = [pizza_num, pizzas[pizza_num-1]]  # 새로운 피자 오븐에 넣어주기
                    pizza_num += 1

    # 남아있는 피자 찾기
    for pizza in oven:
        if pizza != None:
            answer = pizza[0]
    print(f'#{t} {answer}')