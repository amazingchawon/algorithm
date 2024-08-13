# [D2] 4861 회문

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N : 글자판 크기, M : 회문 길이
    arr = [input() for _ in range(N)]   # 글자판, 1차원 배열

    answer = 0

    # 가로 탐색
    for row in arr:
        for i in range(0, N-M+1):  # 문자열 순회, i는 문자열 시작 인덱스
            tmp = row[i:i+M]
            tmp_reversed = tmp[::-1]
            if tmp == tmp_reversed:
                answer = tmp
                break
        if answer != 0:             # 이미 찾았다면, (회문은 1개만 존재)
            break                   # 탐색 종료

    # 세로 배열 만들기
    col_arr = [0] * N

    for i in range(N):
        col = ''
        for j in range(N):
           col += arr[j][i]     # col에 현재 행의 i번 인덱스의 값 추가
        col_arr[i] = col        # col_arr에 현재 열 추가

    # 세로 탐색
    for col in col_arr:
        if answer != 0:             # 이미 찾았다면, (가로 탐색에서 찾았을 것을 대비해 for 문 앞에 배치, 반복횟수 줄이기)
            break                   # 탐색 종료
        for i in range(0, N-M+1):   # 문자열 순회, i는 문자열 시작 인덱스
            tmp = col[i:i+M]
            tmp_reversed = tmp[::-1]
            if tmp == tmp_reversed:
                answer = tmp
                break

    print(f'#{t} {answer}')