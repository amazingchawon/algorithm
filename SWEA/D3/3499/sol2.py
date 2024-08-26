# [D3] 3499 퍼펙트 셔플

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())        # 카드 수
    deck = input().split()  # 처음에 주어진 덱

    answer = []
    d = (N+1)//2

    if N % 2 == 0:
        for i in range(d):
            answer.append(deck[i])
            answer.append(deck[d+i])
    else:
        for i in range(d-1):
            answer.append(deck[i])
            answer.append(deck[d+i])
        answer.append(deck[d-1])

    print(f'#{t}', *answer)