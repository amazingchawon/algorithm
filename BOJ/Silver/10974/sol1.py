# [S3] 10974 모든 순열

# STEP 1. 입력 받기
n = int(input())
arr = [i+1 for i in range(n)]

# STEP 2. 순열 함수 구현
def permutation(arr, n):
    used = [0 for _ in range(n)]

    def generate(chosen, used):
        if len(chosen) == n:
            print(*chosen)
            return

        for i in range(n):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)

# STEP 3. 함수 호출
permutation(arr, n)