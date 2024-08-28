# [D4] 1231 사칙연산

import sys
sys.stdin = open('input.txt', 'r')

def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        if not str(node[n]).isdecimal():                        # 현재 노드 연산자라면,
            child_l = str(node[left[n]])                        # child_l : 현재 노드의 오른쪽 자식
            child_r = str(node[right[n]])                       # child_r : 현재 노드의 오른쪽 자식
            if child_l.isdecimal() and child_r.isdecimal():     # 자식이 둘 다 숫자라면
                child_l, child_r = int(child_l), int(child_r)
                # 연산
                if node[n] == '+':
                    node[n] = child_l + child_r
                elif node[n] == '*':
                    node[n] = child_l * child_r
                elif node[n] == '-':
                    node[n] = child_l - child_r
                else:
                    node[n] = child_l // child_r

T = 10

for t in range(1, T+1):
    N = int(input())      # N : 정점의 개수
    node = [0] * (N+1)    # 노드의 내용을 담을 배열
    left = [0] * (N+1)    # 노드의 왼쪽 자식의 index를 담을 배열
    right = [0] * (N+1)   # 노드의 오른쪽 자식의 index를 담을 배열

    # STEP 1. 이진 트리 만들기
    for i in range(N):
        tmp = input().split()

        # V : 노드 번호, info: 노드에 기록된 정보
        # L, R : 왼쪽 자식 index, 오른쪽 자식 index
        if len(tmp) == 4:
            V, info, L, R = tmp
            V, L, R = int(V), int(L), int(R)
            node[V] = info
            left[V] = L
            right[V] = R
        else:
            V, info = tmp
            V, info = int(V), int(info)
            node[V] = info

    # STEP 2. 연산하기
    post_order(1)

    print(f'#{t} {node[1]}')

