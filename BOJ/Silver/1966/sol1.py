# [S3] 1966 프린터 큐

import sys
input = sys.stdin.readline

from collections import deque

# STEP 1. 입력 받기
T = int(input())                    # T : 테케 수

for _ in range(T):
    N, M = map(int, input().split())    # N : 문서 개수, M : 처음 문서 위치
    nums = deque(map(int, input().split()))

    cnt = 1
    target = (nums[M], M)
    printer_q = deque((nums[i], i) for i in range(N))

    while printer_q:
        max_num = max(printer_q, key=lambda x:x[0])
        front = printer_q.popleft()
        if front == max_num:
            if front == target:
                print(cnt)
                break
            else:
                cnt += 1
        else:
            printer_q.append(front)