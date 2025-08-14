# [S1] 11286 절댓값 힙

import sys
input = sys.stdin.readline

import heapq

# STEP 1. 변수 할당
N = int(input())
abs_nums = []
nums = []

for _ in range(N):
    prompt = int(input())

    # 출력하는 경우,
    if prompt == 0:
        if len(nums) == 0:  # 비어있는 경우,
            print(0)        # 0 출력
        else:
            min_num = heapq.heappop(abs_nums)   # 절댓값이 제일 작은 값 출력

            if -min_num in nums:                # 같은 절댓값이면 음수를 출력
                print(nums.pop(nums.index(-min_num)))
            else:
                print(nums.pop(nums.index(min_num)))

    # 추가하는 경우,
    else:
        heapq.heappush(abs_nums, abs(prompt))   # 힙으로 절댒값만 저장
        nums.append(prompt)