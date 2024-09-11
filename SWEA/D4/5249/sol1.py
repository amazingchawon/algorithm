# [D4] 5249 최소 신장 트리

import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


T = int(input())

for t in range(1, T+1):
    # V: 마지막 노드 번호 (0번부터 V번, 총 V+1 개), E: 간선 수
    V, E = map(int, input().split())

    # STEP 1. 간선 정보 기록
    edge = [0] * E
    for i in range(E):
        n1, n2, w = map(int, input().split())
        edge[i] = (n1, n2, w)

    edge.sort(key=lambda x: x[2])

    # STEP 2. union-find 활용, MST 만들기
    # 대표 원소 배열
    parents = [i for i in range(V+1)]   # 마지막 노드번호가 V!! +1 까먹지 않도록 주의

    # cnt : 간선 수, 노드 개수 - 1이 되면 신장 트리 완성
    # total : 가중치 합산할 변수
    cnt = 0
    total = 0

    for n1, n2, w in edge:
        if find_set(n1) != find_set(n2):
            cnt += 1
            union(n1, n2)
            total += w
            if cnt == V:
                break

    print(f'#{t} {total}')