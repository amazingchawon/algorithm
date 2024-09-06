# [A형기출] 2105 디저트 카페

# import sys
# sys.stdin = open('input.txt', 'r')

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

T = int(input())

for t in range(1, T+1):
    # N : 지역 크기, cafes : 파는 디저트의 종류가 기록된 이차원 배열
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    answer = -1

    # STEP 1. (x, y) 카페에서 투어할 수 있는 가장 긴 길이 찾기
    # 투어 방향 :
    # (4) 위/아래\ (1)
    # (3) 위\아래/ (2)
    for x in range(N-1):                # N-1 : 마지막 줄에서 투어 시작 불가
        for y in range(1, N-1):         # 1, N-1: 행의 시작, 끝에서 투어 시작 불가
            nx, ny = x, y
            visited = {cafes[nx][ny]}
            # 4방향 탐색
            for i in range(4):
                cnt = 0
                while 0 <= nx+dx[i] < N and 0 <= ny+dy[i] < N:      # 다음 탐색할 카페가 범위 안이고,
                    if nx+dx[i] == x and ny+dy[i] == y and i == 3:  # 원점으로 돌아가는 상황이라면,
                        nx, ny = nx + dx[i], ny + dy[i]
                        cnt += 1
                        break
                    if cafes[nx+dx[i]][ny+dy[i]] not in visited and ((nx+dx[i], ny+dy[i]) not in [(0, 0), (0, N-1), (N-1, 0), (N-1, N-1)]):    # 아직 안 먹어본 디저트를 판다면,
                        nx, ny = nx + dx[i], ny + dy[i]
                        visited.add(cafes[nx][ny])
                        cnt += 1
                    # 먹어본 디저트여서 못가는데, 아직 해당 방향으로 한칸도 못 움직인 상황이라면,
                    # 한칸 뒤로 가기
                    # 만약 i가 0이라면 -> 해당 칸에서는 투어 불가한 것이므로 예외처리
                    else:
                        if cnt == 0 and i > 0:
                            visited.remove(cafes[nx][ny])
                            nx, ny = nx - dx[i-1], ny - dy[i-1]
                            # 만약 한 칸 뒤로 가서 출발 지점으로 돌아간거라면, 투어 불가한 것
                            # x, y에서 투어 종료
                            if nx == x and ny == y:
                                break
                        else:
                            break
                if cnt == 0:            # 해당 방향으로 한 칸이라도 안 움직였으면 현재 칸에서 투어 불가
                    break
                if nx == x and ny == y:
                    if answer < len(visited):
                        answer = len(visited)

    print(f'#{t} {answer}')