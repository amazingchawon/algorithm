# [D3] 4615 재미있는 오셀로 게임

import sys
sys.stdin = open('input.txt', 'r')

# 1이면 흑돌, 2이면 백돌
B = 1
W = 2
flip = [0, 2, 1]

# 함수 구현
def game(x, y, color):
    board[x][y] = color  # 돌 놓기
    # 델타 탐색
    for dx, dy in [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]:
        nx, ny = x + dx, y + dy  # 다음 칸
        chip_to_flip = []  # 뒤집을 돌 저장할 배열
        while 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] == flip[color]:  # 범위 안이고 색이 다르면
            chip_to_flip.append([nx, ny])
            nx, ny = nx + dx, ny + dy
        if 1 <= nx <= N and 1 <= ny <= N and board[nx][ny] == color:  # 같은 색을 만난 거라면
            for chip in chip_to_flip:  # 뒤집기
                board[chip[0]][chip[1]] = flip[board[chip[0]][chip[1]]]

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N : 오셀로 보드 크기, M : 돌을 놓는 횟수
    play = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * (N+1) for _ in range(N+1)] # 보드 준비, 1-N 인덱스 사용
    # 중심부 돌 배치
    board[N//2][N//2] = W
    board[N//2 + 1][N//2] = B
    board[N//2][N//2 + 1] = B
    board[N//2 + 1][N//2 + 1] = W

    for col, row, color in play:
        game(row, col, color)

    black = 0
    white = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == B:
                black += 1
            elif board[i][j] == W:
                white += 1

    print(f'#{t} {black} {white}')