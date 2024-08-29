# [D2] 4881 배열 최소 합

import sys
sys.stdin = open('input.txt', 'r')


def permutation(arr, r):
    used = [0] * r                      # 원소를 사용했는지 안했는지 판단할 배열
    result = [10*N + 1]                 # 순열 최소합 저장 변수
    tmp, idx = [0], [0]

    def generate(used):
        if tmp[0] >= result[0]:
            return
        if idx[0] == r:                 # r 길이의 순열이 만들어졌다면,
            if result[0] > tmp[0]:
                result[0] = tmp[0]
            return                      # 종료
        for i in range(r):
            if not used[i]:                     # 해당 원소 아직 사용 안했다면,
                tmp[0] += arr[idx[0]][i]        # 원소 더해주기
                idx[0] += 1
                used[i] = 1                     # 사용 기록 남기기
                generate(used)                  # 현재 원소가 들어간 순열 만들기
                used[i] = 0                     # 사용 기록 없애기
                idx[0] -= 1
                tmp[0] -= arr[idx[0]][i]

    generate(used)
    return result

T = int(input())

for t in range(1, T+1):
    N = int(input())    # N*N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    perms = permutation(arr, N)

    answer = perms[0]


    print(f'#{t} {answer}')