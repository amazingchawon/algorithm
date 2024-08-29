# [D2] 5174 subtree

import sys
sys.stdin = open('input.txt', 'r')

def in_order(node):
    global cnt
    if node:        # node가 비어있지 않다면,
        in_order(left[node])
        cnt += 1
        in_order(right[node])

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())        # E : 간선 수, N : 탐색할 노드
    data = list(map(int, input().split()))  # 간선 정보가 담긴 배열
    nodes_num = max(data)
    left = [0] * (nodes_num+1)
    right = [0] * (nodes_num+1)


    # STEP 1. 트리 채우기
    for i in range(0, len(data), 2):
        V = data[i]
        if left[V] == 0:                         # 왼쪽 노드가 비어있다면,
            left[V] = data[i+1]             # 채우기
        else:
            right[V] = data[i+1]            # 오른쪽 노드 채우기

    cnt = 0
    # STEP 2. 탐색
    in_order(N)

    print(f'#{t} {cnt}')