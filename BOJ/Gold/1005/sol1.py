# [G3] 1005 ACM Craft
import sys
from collections import deque

input = sys.stdin.readline

# STEP 1. 입력 받기
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())    # N: 건물 수, K: 건설 규칙 수
    cost = [0] + list(map(int, input().split()))

    order = [[] for _ in range(N + 1)]  # order[x]: x가 선행 조건인 건물들
    count = [0] * (N+1)                 # count[x]: x번째 건물을 짓기 전 지어야하는 건물 수

    for i in range(K):
        x, y = map(int, input().split())
        order[x].append(y)
        count[y] += 1

    W = int(input())

    # STEP 2. 건물 짓기
    q = deque()                 # 짓고 있는 건물 관리
    time_spent = [0] * (N+1)    # time_spent[x] : x번째 건물을 짓기 위한 최소 시간

    # STEP 2.1. 선행 건물 조건이 없는 건물 짓기
    for i in range(1, N+1):
        if count[i] == 0:
            q.append(i)
            time_spent[i] = cost[i]

    while q:
        cur = q.popleft()

        for nxt in order[cur]:
            time_spent[nxt] = max(time_spent[nxt], time_spent[cur] + cost[nxt])
            count[nxt] -= 1

            if count[nxt] == 0:
                q.append(nxt)

    print(time_spent[W])