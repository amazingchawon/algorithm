# [S1] 15903 카드 합체 놀이

import sys

# STEP 1. 입력받기
n, m = map(int, sys.stdin.readline().split())           # n: 카드 장수 m: 게임 횟수
cards = list(map(int, sys.stdin.readline().split()))

# STEP 2. 최소값 계산
for _ in range(m):
    cards.sort()
    tmp = cards[0] + cards[1]
    cards[0], cards[1] = tmp, tmp

print(sum(cards))