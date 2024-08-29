# [D2] 4881 배열 최소 합
# 메모리 초과

import sys
sys.stdin = open('input.txt', 'r')


def permutation(arr, r):
    used = [0] * len(arr)               # 원소를 사용했는지 안했는지 판단할 배열
    result = []                         # 만들어진 순열을 담을 배열

    def generate(chosen, used):
        if len(chosen) == r:            # r 길이의 순열이 만들어졌다면,
            result.append(chosen[:])
            return                      # 만들어진 순열 반환
        for i in range(len(arr)):
            if not used[i]:             # 해당 원소 아직 사용 안했다면,
                chosen.append(arr[i])   # 순열에 추가
                used[i] = 1             # 사용 기록 남기기
                generate(chosen, used)  # 현재 원소가 들어간 순열 만들기
                chosen.pop()            # 순열에서 빼기
                used[i] = 0             # 사용 기록 없애기

    generate([], used)
    return result

T = int(input())

for t in range(1, T+1):
    N = int(input())    # N*N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    number = [i for i in range(N)]

    perms = permutation(number, N)

    answer = 10*N + 1   # 모든 칸이 10로 차있는 배열의 합보다 1 큰 수로 초기화

    for perm in perms:      # 가능한 모든 순열 중 1개 꺼내기
        tmp = 0             # 현재 순열의 순서대로 더했을 떄 배열 합 저장할 변수
        for i in range(N):
            tmp += arr[i][perm[i]]  # i번째 줄에 perm[i]번째 수 선택해서 더해주기
        if answer > tmp:
            answer = tmp

    print(f'#{t} {answer}')