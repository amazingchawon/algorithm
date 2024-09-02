# [D3] 5189 전자카트

import sys
sys.stdin = open('input.txt', 'r')


def permutation(perm, used):
    global answer
    if len(perm) == N-1:                        # 순열 다 만들었다면,
        tmp = arr[0][perm[0]]                   # 사무실에서 관리실로 출발
        for i in range(1, len(perm)):           # 관리실 돌아다니기
                tmp += arr[perm[i-1]][perm[i]]
        tmp += arr[perm[i]][0]                  # 관리실에서 사무실로 돌아가기
        if answer > tmp:
            answer = tmp
        return
    for i in range(1, len(arr)):
        if not used[i]:
            perm.append(i)
            used[i] = 1
            permutation(perm, used)
            perm.pop()
            used[i] = 0

T = int(input())

for t in range(1, T+1):
    N = int(input())    # N : 사무실 + 관리구역 수
    arr = [list(map(int, input().split())) for _ in range(N)]   # arr : 배터리 사용량

    used = [0] * N
    answer = 100 * N + 1    # 답 저장 변수, 가능한 최대 배터리 사용량으로 초기화
    permutation([], used)

    print(f'#{t} {answer}')