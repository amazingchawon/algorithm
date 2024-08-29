# [D3] 5178 노드의 합

import sys
sys.stdin = open('input.txt', 'r')

def post_order(n):
    if n <= N:
        post_order(2*n)         # 왼쪽 자식
        post_order(2*n + 1)     # 오른족 자식
        if nodes[n] == 0:       # 0이 기록되어있다면! -> 더할 차례
            if 2*n+1 <= N:      # 오른쪽 자식이 존재한다면,
                nodes[n] = nodes[2*n] + nodes[2*n+1]
            else:               # 존재하지 않는다면,
                nodes[n] = nodes[2*n]

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    
    # STEP 1. 이진 트리의 leaf node에 값 넣기
    nodes = [0] * (N+1)

    for i in range(M):
        V, info = map(int, input().split())     # V : 정점 index, info : 기록된 수
        nodes[V] = info
    
    # STEP 2. 후위 순회
    post_order(L)
    answer = nodes[L]

    print(f'#{t} {answer}')

