# [D3] 3499 퍼펙트 셔플

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())        # 카드 수
    deck = input().split()  # 처음에 주어진 덱

    if N % 2 == 0:                                      # N이 짝수라면
        deck1, deck2 = deck[:N//2], deck[N//2:]     # 절반 나누기
    else:                                               # N이 홀수라면
        deck1, deck2 = deck[:N//2+1], deck[N//2+1:]     # deck1 번에 1장 더 주기

    answer = []

    for i in range(len(deck2)):
        answer.append(deck1.pop(0))
        answer.append(deck2.pop(0))

    answer += deck1

    print(f'#{t}', end=" ")
    print(*answer)