# [D3] 1220 Magnetic

import sys
sys.stdin = open('input.txt', 'r')

T = 10

N, S = 1, 2

for t in range(1, T+1):
    SIZE = int(input())    # 자석판 크기, 항상 100으로 주어짐
    arr = [list(map(int, input().split())) for _ in range(SIZE)] # 자석판 만들기

    answer = 0

    # 교착 상태 수 세기
    # 0을 뺴고 12 개수 == 교착 상태에 빠진 자석의 수
    for y in range(SIZE):
        col = ''
        for x in range(SIZE):
            if arr[x][y] != 0:          # 0이 아니면
                col += str(arr[x][y])   # 더해주기
        answer += col.count('12')

    print(f'#{t} {answer}')