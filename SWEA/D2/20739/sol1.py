# [D2] 20739 고대 유적2

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N, M : 가로 * 세로 길이
    arr = [input().split() for _ in range(N)]

    answer = 0

    # 가로 탐색
    for x in range(N):
        row = ''                # 리스트를 하나의 문자열로 저장하는 변수
        for y in range(M):
            row += arr[x][y]    # 해당 인덱스의 문자를 문자열에 저장
        tmp = row.split('0')    # tmp에 0으로 구분하여 저장
        for structure in tmp :
            if len(structure) > 1 and len(structure) > answer:      # 길이가 1 이상인 구조물이 있고, 현재 저장된 구조물보다 길다면,
                answer = len(structure)                             # 갱신

    # 세로 탐색
    for y in range(M):
        col = ''                # 리스트를 하나의 문자열로 저장하는 변수
        for x in range(N):
            col += arr[x][y]    # 해당 인덱스의 문자를 문자열에 저장
        tmp = col.split('0')    # tmp에 0으로 구분하여 저장
        for structure in tmp:
            if len(structure) > 1 and len(structure) > answer:      # 길이가 1 이상인 구조물이 있고, 현재 저장된 구조물보다 길다면,
                answer = len(structure)                             # 갱신

    print(f'#{t} {answer}')