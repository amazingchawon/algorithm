# [S1] 11286 절댓값 힙

import sys
input = sys.stdin.readline

import heapq

# STEP 1. 변수 할당
N = int(input())
nums = []

for _ in range(N):
    x = int(input())

    # 추가하는 경우
    if x:
        if x > 0:
            heapq.heappush(nums, (x, x))    # 양수일 떄, (절댓값, 양수)
        else:
            heapq.heappush(nums, (-x, x))   # 음수일 떄, (절댓값, 음수)
    else:
        if nums:
            print(heapq.heappop(nums)[1])           # 인덱식 -> 원본 수 출력
        else:
            print(0)