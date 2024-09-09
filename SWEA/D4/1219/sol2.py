# [D4] 1219 길찾기

import sys
sys.stdin = open('input.txt', 'r')

def search(node):
    global answer
    visited[node] = 1

    for next in range(100):
        if adj_lst[node][next] and visited[next] == 0:
            if next == 99:
                answer = 1
                return
            search(next)


T = 10

for t in range(T):
    # num : 테케 번호, road_num : 길의 수
    num, road_num = map(int, input().split())
    roads = list(map(int, input().split()))

    # STEP 1. 인접행렬 만들기
    adj_lst = [[0] * 100 for _ in range(100)]

    for i in range(road_num):
        x = roads[2*i]
        y = roads[2*i + 1]
        adj_lst[x][y] = 1

    # STEP 2. DFS 재귀로 구현 -> 함수 호출 결과 반환
    visited = [0] * 100
    answer = 0
    search(0)

    print(f'#{num} {answer}')