# [S2] 1927 최소 힙
# heapq 모듈 사용

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)