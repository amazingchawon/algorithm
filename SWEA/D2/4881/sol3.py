# [D2] 4881 배열 최소 합
# min_s 문제. 다시 풀려면 generate에서 idx == r부분을 밖으로 빼와야 한다!

import sys
sys.stdin = open('input.txt', 'r')


def permutation(arr, r):
    used = [0] * r                      # 원소를 사용했는지 안했는지 판단할 배열
    tmp_sum = 0
    min_sum = 10*r + 1
    idx_arr = 0

    def generate(tmp, min_s, idx, used):
        if tmp >= min_s:
            return min_s
        if idx == r:                            # r 길이의 순열이 만들어졌다면,
            if min_s > tmp:
                min_s = tmp
            return min_s                        # 종료
        for i in range(r):
            if not used[i]:                     # 해당 원소 아직 사용 안했다면,
                tmp += arr[idx][i]              # 원소 더해주기
                idx += 1
                used[i] = 1                     # 사용 기록 남기기
                generate(tmp, min_s, idx, used) # 현재 원소가 들어간 순열 만들기
                used[i] = 0                     # 사용 기록 없애기
                idx -= 1
                tmp -= arr[idx][i]
        return min_s

    min_sum = generate(tmp_sum, min_sum, idx_arr, used)
    return min_sum

T = int(input())

for t in range(1, T+1):
    N = int(input())    # N*N 배열
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp_sum, idx = 0, 0
    min_sum = 10 * N + 1
    MAXC = 3

    answer = permutation(arr, N)


    print(f'#{t} {answer}')