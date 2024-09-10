# [D3] 5248 그룹 나누기

import sys
sys.stdin = open('input.txt', 'r')


def find_set(x):
    if x == students[x]:
        return x
    else:
        students[x] = find_set(students[x])
        return students[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    # 작은 학생이 팀장이 되도록 합치기
    if root_x < root_y:
        students[root_y] = root_x
    else:
        students[root_x] = root_y


T = int(input())

for t in range(1, T + 1):
    # N : 학생 수, M : 쪽지 수
    # pairs : 쪽지 내용
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))

    # STEP 1. 팀 만들어주기
    students = [i for i in range(N + 1)]        # i번쨰 학생은 students[i] 학생의 팀에 속함

    for p in range(M):
        # STEP 2. union, find_set 구현
        union(pairs[p * 2], pairs[p * 2 + 1])  # 팀 만들어주기

    for i in range(1, N+1):
        find_set(i)

    answer = len(set(students[1:]))             # 0번째 학생은 없으니까 지워주기
    print(f'#{t} {answer}')
