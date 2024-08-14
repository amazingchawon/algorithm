# [D3] 5099 피자 굽기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # 인덱스까지 같이 저장
    pizzas = [[idx, val] for idx, val in enumerate(list(map(int, input().split())), 1)]
    oven = []

    for i in range(N):                    # 오븐에 피자 꽉채우기
        oven.append(pizzas.pop(0))
    while len(oven) > 1:                # 오븐에 피자 1개가 남을때까지
        pizza = oven.pop(0)             # 제일 먼저 넣은 피자를 빼보기
        pizza[1] //= 2                  # 치즈 녹이기
        if pizza[1]:                    # 피자에 치즈가 다 안녹았다면,
            oven.append(pizza)          # 다시 오븐에 넣기
        if pizzas and len(oven) != N:   # 피자는 남았는데 오븐이 비었다면,
            oven.append(pizzas.pop(0))  # 오븐에 새 피자 추가

    print(f'#{t} {oven[0][0]}')
