# [D2] 5102 노드의 거리

import sys
sys.stdin = open('input.txt', 'r')

def BFS(start, end, arr):
    # 준비
    visited = [0] * (V + 1)     # 노드 방문 기록 배열, 노드 번호는 1번부터 존재 -> V + 1
    queue = [start]
    visited[start] = 1
    # 탐색
    while queue:
        current = queue.pop(0)                                      # 현재 방문 노드
        for nxt in range(len(arr)):                                 # 노드 순회
            if nxt == end and arr[current] == 1:                    # 현재 노드에서 도착 지점에 갈 수 있다면,
                tmp = visited[current] + 1                          # 현재 루트로 탐색했을 때, 도착지까지 이동 횟수
                if visited[nxt] != 0 and tmp > visited[nxt]:        # 이미 방문했었고, 현재 루트로 탐색했을 때 이동 횟수가 크다면,
                    pass                                            # 패스
                else:                                               # 현재 루트로 탐색했을 떄 이동횟수가 더 작거나, 방문하지 않은 경우
                    visited[nxt] = tmp                              # 갱신
            if arr[current][nxt] == 1 and visited[nxt] == 0:        # 현재 방문한 노드와 현재 순회중인 노드가 연결되어 있고, 방문한 적이 없다면,
                queue.append(nxt)                                   # 인큐
                visited[nxt] = visited[current] + 1                 # 방문할 떄 걸리는 거리 기록
    return visited[end]

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())                # V : 노드 개수, E : 간선 개수
    adj_list = [[0] * (V+1) for _ in range(V+1)]    # 간선 데이터 저장할 2차원 배열

    # 간선 데이터 저장
    for i in range(E):
        x, y = map(int, input().split())            # 노드 1, 노드 2
        adj_list[x][y] = 1                          # 방향성 X, 양쪽에 기록
        adj_list[y][x] = 1

    S, G = map(int, input().split())                # S : 시작 노드, G : 도착 노드

    answer = BFS(S, G, adj_list)

    if answer != 0 :    # S -> G 가능하다면
        answer -= 1     # 처음 시작한 곳도 이동횟수를 카운트 했음 -> -1 해주기

    print(f'#{t} {answer}')