# [D4] 1231 중위 순회

import sys
sys.stdin = open('input.txt', 'r')

def inorder(node):
    if node:
        inorder(left[node])
        print(parent[node], end="")
        inorder(right[node])
T = 10

for t in range(1, T+1):
    N = int(input())

    left = [0] * (N+1)      # 왼쪽 자식 노드 기록
    right = [0] * (N+1)     # 오른쪽 자식 노드 기록
    parent = [0] * (N+1)    # 부모 자식의 info 기록

    # STEP1. Tree 구조 만들기
    for i in range(N):
        data = input().split()
        # V : 부모 노드의 index, info : 부모 노드에 기록된 데이터
        # L, R : 왼쪽/오른쪽 자식 노드의 index
        if len(data) == 4:
            V, info, L, R = data
            V, L, R = int(V), int(L), int(R)  # index 값으로 사용하기 위해 int형으로 변환
            left[V] = L
            right[V] = R
            parent[V] = info
        elif len(data) == 3:
            V, info, L = data
            V, L = int(V), int(L)
            left[V] = L
            parent[V] = info
        else:
            V, info = data
            V = int(V)
            parent[V] = info

    # STEP2. 순회
    print(f'#{t}', end=" ")
    inorder(1)
    print()