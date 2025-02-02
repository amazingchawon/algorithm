# [G5] 11000 강의실 배정

import heapq
import sys
input = sys.stdin.readline

N = int(input())
room = []           # 종료 시간 담을 배열

# STEP 1. 시작 시간 순으로 강의 정렬
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[0])

# STEP 2. 강의 종료 시간 비교
heapq.heappush(room, lectures[0][1])    # 힙에 첫번째로 시작하는 강의의 T(강의 종료 시간) 삽입

for i in range(1, N):
    if lectures[i][0] < room[0]:             # 현재 강의의 시작 시간이 가장 빨리 끝나는 강의 시간보다 짧으면
        heapq.heappush(room, lectures[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lectures[i][1])

print(len(room))