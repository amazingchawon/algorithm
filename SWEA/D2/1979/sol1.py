# [D2] 1979 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [input().replace(' ', '') for _ in range(N)]

    answer = 0

    # 가로 탐색
    puzzle_hori = [puzzle[i].split('0') for i in range(N)]  # 0으로 나누기
    for row in puzzle_hori:
        for i in range(len(row)):
            if row[i] == '1'*K:     # 1이 k개 붙어있는 문자열 존재 ==  단어를 넣을 수 있다
                answer += 1
    # 세로 탐색
    # puzzle 세로 -> puzzle 가로로 재배열
    puzzle_ver = [''] * N
    for i in range(N):
        for j in range(N):
            puzzle_ver[i] += puzzle[j][i]

    puzzle_ver = [puzzle_ver[i].split('0') for i in range(N)]  # 0으로 나누기
    for row in puzzle_ver:
        for i in range(len(row)):
            if row[i] == '1'*K:     # 1이 k개 붙어있는 문자열 존재 ==  단어를 넣을 수 있다
                answer += 1

    print(f'#{t} {answer}')