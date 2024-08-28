# [D2] 5177 이진 힙

import sys
from heapq import heappush

sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())    # N : 노드 수
    arr = list(map(int, input().split()))  # arr : 노드 값
    heap = []

    # STEP 1. 힙에 값 넣기
    for num in arr:
        heappush(heap, num)

    # STEP 2. 마지막 노드의 조상 노드들 합 구하기
    answer = 0          # 합 저장 변수
    child = len(heap)   # 마지막 노드의 인덱스
    parent = child//2   # 부모 노드의 인덱스

    while parent >= 1:  # root 노드에 도달할 때까지 순회
        answer += heap[parent-1]    # 더해주기
        parent //= 2    # 현재 노드의 부모 노드로 이동

    print(f'#{t} {answer}')