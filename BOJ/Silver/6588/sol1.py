# [S1] 6588 골드바흐의 추측

import sys

# STEP 1. 에라토스테네스의 체로 백만 이하 소수 판별
is_prime = [1] * 1000001
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(1000000**0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, 1000001, i):
            is_prime[j] = 0

# STEP 2. 전체 테스트 케이스 입력
inputs = sys.stdin.read().splitlines()

# STEP 2. 테스트 케이스 대상으로 추측 점증
for tc in inputs:
    N = int(tc)
    if N == 0:
        break

    found = False
    for num in range(3, N // 2 + 1, 2):
        if is_prime[num]:
            tmp = N - num
            if is_prime[tmp]:
                print(f'{N} = {num} + {tmp}')
                found = True
                break

    if not found:
        print("Goldbach's conjecture is wrong.")