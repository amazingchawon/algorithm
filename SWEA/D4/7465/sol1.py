# [D4] 7465 창용 마을 무리의 개수

import sys
sys.stdin = open('input.txt', 'r')


def find(x):
    if x == people[x]:
        return x
    else:
        people[x] = find(people[x])
        return people[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    # 번호가 작은 사람이 무리의 대표 되게끔
    if root_x < root_y:
        people[root_y] = root_x
    else:
        people[root_x] = root_y


T = int(input())

for t in range(1, T+1):
    # N: 마을 사람 수, M: 관계 수
    N, M = map(int, input().split())
    people = [i for i in range(N+1)]    # 마을 사람 1번 ~ N번, 나중에 0번 버려야 함

    # STEP 1. 아는 사람들 무리 만들어주기
    for m in range(M):
        x, y = map(int, input().split())
        union(x, y)

    # STEP 2. people에 무리의 짱짱 대표가 기록되게 find 한번 더 돌려주기
    for p in range(1, N+1):             # 0번 사람 무시
        find(p)

    answer = len(set(people[1:]))
    print(f'#{t} {answer}')