# [G5] 15486 퇴사 2

import sys
input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1) # 1일부터 N일

for i in range(1, N+1):
    t, p = map(int, input().split())                        # t : 걸리는 시간, p : 작업량

    DP[i] = max(DP[i], DP[i - 1])                           # i번째 일에 할 수 있는 작업량 중 제일 큰걸로 갱신해줌

    if i + t - 1 < N + 1:                                   # i일에 시작해서 t일 걸리는 상담을 할 수 있는 경우
        DP[i + t - 1] = max(DP[i + t - 1], DP[i - 1] + p)   # 원래 있던 값이 큰지, 아니면 갱신하는 게 큰지 체크

print(max(DP))