# [A형기출] 2105 디저트 카페

import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def DFS(x, y, idx):
    stack = [(x, y)]
    visited = {cafes[x][y]} # 먹은 디저트 종류를 기록할 리스트
    cycle = False

    while stack and cycle == False:
        tx, ty = stack.pop()

        # 방문 안했고, 도달 불가지역이 아니라면,
        if cafes[tx][ty] not in visited and (tx, ty) not in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]:
            visited.add(cafes[tx][ty])
            # 현재 카페에서 이동할 수 있는 카페를 스택에 추가
            # 현재 이동방향이 아래\이라면
            if idx == 0:
                # 다음 방향 추가
                if 0 <= tx + dx[1] < N and 0 <= ty + dy[1] < N:
                    stack.append((tx + dx[1], ty + dy[1]))
                # 현재 방향 지속
                if 0 <= tx + dx[0] < N and 0 <= ty + dy[0] < N:
                    stack.append((tx + dx[0], ty + dy[0]))
            elif idx == 1:
                # 다음 방향 추가
                if 0 <= tx + dx[2] < N and 0 <= ty + dy[2] < N:
                    stack.append((tx + dx[2], ty + dy[2]))
                # 현재 방향 지속
                if 0 <= tx + dx[1] < N and 0 <= ty + dy[1] < N:
                    stack.append((tx + dx[1], ty + dy[1]))
            elif idx == 2:
                # 다음 방향 추가
                if 0 <= tx + dx[3] < N and 0 <= ty + dy[3] < N:
                    stack.append((tx + dx[3], ty + dy[3]))
                # 현재 방향 지속
                if 0 <= tx + dx[2] < N and 0 <= ty + dy[2] < N:
                    stack.append((tx + dx[2], ty + dy[2]))
            else:
                # 다음 방향 추가
                if 0 <= tx + dx[3] < N and 0 <= ty + dy[3] < N:
                    stack.append((tx + dx[3], ty + dy[3]))

T = int(input())

for t in range(1, T+1):
    # N : 지역 크기, cafes : 파는 디저트의 종류가 기록된 이차원 배열
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    answer = -1