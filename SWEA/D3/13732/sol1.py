# [D3] 13732 정사각형 판정

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    answer = 'no'

    # STEP 1. 막힌 칸(#) 개수 세기
    # 막힌 칸이 제곱수가 아니라면 정사각형이 될 수 없음
    cnt = 0
    for row in arr:
        for block in row:
            if block == '#':
                cnt += 1

    # STEP 2 . cnt가 제곱수가 맞는지 확인
    size = cnt ** 0.5                       # size : 루트 cnt
    if size % 1 == 0:                       # 제곱수가 맞다면!
        size = int(size)
        for i in range(0, N-size+1):        # arr에서 똑같은 문자열이 연속해서 size개 나온다면 정사각형 조건 달성
            line = arr[i]
            if line.count('#') > 0 :
                for j in range(1, size):
                    if line == arr[i+j]:
                        # 정사각형 맞다
                        continue
                    else:
                        break
                else:
                    answer = 'yes'

    print(f'#{t} {answer}')