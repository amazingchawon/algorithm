# [D2] 1974 스도쿠 검증

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):

    sudoku = [input().split() for _ in range(9)]    # 스도쿠 만들기

    answer = 1  # 정답일 시를 가정하고 초기화

    # 스도쿠 순회
    # 가로 세로 순회
    for x in range(9):
        # 가로 체크
        row = set(sudoku[x])
        if len(row) != 9:
            answer = 0
            break

        # 세로 체크
        col = set()
        for y in range(9):
            col.add(sudoku[y][x])

        if len(col) != 9:          # 세로줄 중복 제거시 9개가 아니라면
            answer = 0                  # 오답
            break

    if answer == 1: # 가로 세로 검사 통과헀다면,
        # 3X3 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_3X3 = set()                          # 3X3 저장 변수
                for k in range(3):                          # 3개씩 순회하기 위해
                    for l in range(3):
                        square_3X3.add(sudoku[i+k][j+l])

            if len(square_3X3) != 9:       # 3X3 중복 제거시 9개가 아니라면,
                answer = 0
                break

            if answer == 0:
                break

    print(f'#{t} {answer}')