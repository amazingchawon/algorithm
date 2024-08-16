# [D3] 6485 삼성시의 버스 노선

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    routes = [0] * N

    for i in range(N): # 노선 기록
        routes[i] = list(map(int, input().split()))

    P = int(input()) # P : 버스 정류장 개수
    answer = [0] * P

    for i in range(P):
        stop = int(input())
        for route in routes:
            if route[0] <= stop <= route[1]:    # 범위 안이면
                answer[i] += 1

    print(f'#{t}', end=' ')
    print(*answer)