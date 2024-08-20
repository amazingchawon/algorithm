# [D3] 6019 기차 사이의 파리

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # D : 기차 사이의 거리
    # A, B : 기차 A, B의 속력
    # F : 파리의 속력
    D, A, B, F = map(int, input().split())

    # 파리의 이동 시간 == 두 기차가 충돌할 때까지 걸리는 시간 * 파리의 속력
    time = D / (A+B)   # 두 기차가 충돌할 때까지 걸리는 시간
    answer = F * time

    print(f'#{t} {answer}')