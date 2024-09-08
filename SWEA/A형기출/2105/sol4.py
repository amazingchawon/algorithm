# [A형기출] 2105 디저트 카페
# 재귀로 구현 - PASS 코드

import sys
sys.stdin = open('input.txt', 'r')

dx = [1, 1, -1, -1, 0]
dy = [1, -1, -1, 1, 0]

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

def tour(start, current, visited, dir_idx):
    '''
    :param start: 투어 시작 장소 좌표
    :param current: 현재 투어 중인 카페 좌표
    :param visited: 들린 카페 기록하는 set
    :param dir_idx: 현재 투어 방향 idx
    투어 방향 :
    (3) 위/아래\ (0)
    (2) 위\아래/ (1)
    '''
    global answer
    if visited and start == current:
        if answer < len(visited):
            answer = len(visited)
    elif dir_idx == 4:
        return

    tx, ty = current

    if 0 <= tx < N and 0 <= ty < N:
        if cafes[tx][ty] in visited:
            return
        else:
            visited.add(cafes[tx][ty])

        tour(start, (tx + dx[dir_idx], ty+ dy[dir_idx]), visited, dir_idx)
        tour(start, (tx + dx[dir_idx], ty + dy[dir_idx]), visited, dir_idx+1)
        visited.remove(cafes[tx][ty])

T = int(input())

for t in range(1, T+1):
    # N : 지역 크기, cafes : 파는 디저트의 종류가 기록된 이차원 배열
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    answer = -1

    for x in range(N-1):
        for y in range(1, N-1):
            tour((x, y), (x, y), set(), 0)

    print(f'#{t} {answer}')