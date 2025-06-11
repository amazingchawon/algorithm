# [S3] 15649 N과 M (1)

# STEP 0. 순열 함수 구현
def permutation(arr, r):
    used = [0 for _ in range(len(arr) + 1)]

    def generate(chosen, used):
        if len(chosen) == r:
            print(*chosen)
            return

        for i in range(1, len(arr)+1):
            if not(used[i]):
                chosen.append(i)
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]        # 1-N 포함된 배열 만들기

# STEP 2. 1-N까지 자연수 중 중복 없이 M개 고르기 -> 순열
permutation(arr, M)