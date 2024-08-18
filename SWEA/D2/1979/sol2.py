# [D2] 1979 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]

    answer = 0

    for x in range(N):
        cnt_row = 0                     # 가로 1 개수 카운트 변수
        cnt_col = 0                     # 세로 1 개수 카운트 변수
        for y in range(N):
            # 가로 탐색
            if puzzle[x][y] == '1':     # 현재 탐색 칸이 1일떄,
                cnt_row += 1            # 1 개수 카운트 증가
                if (y == N-1 or puzzle[x][y+1] == '0') and cnt_row == K :   # 마지막 칸이거나, 다음 칸이 0이고 and 1이 K 만큼 있다면,
                    answer += 1
            else:                       # 현재 탐색 칸 0일때,
                cnt_row = 0

            # 세로 탐색
            if puzzle[y][x] == '1':  # 현재 탐색 칸이 1일떄,
                cnt_col += 1  # 1 개수 카운트 증가
                if (y == N - 1 or puzzle[y+1][x] == '0') and cnt_col == K:  # 마지막 칸이거나, 다음 칸이 0이고 and 1이 K 만큼 있다면,
                    answer += 1
            else:  # 현재 탐색 칸 0일때,
                cnt_col = 0

    print(f'#{t} {answer}')