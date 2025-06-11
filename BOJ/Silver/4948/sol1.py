# [S2] 4948 베테르랑 공준

# STEP 1. 에라토스테네스의 체 구현
is_prime = [1 for _ in range(123456*2 + 1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(((123456*2) + 1)*0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, 123456*2 + 1, i):
            is_prime[j] = 0

while True:
    N = int(input())

    # 종료조건
    if N == 0:
        break

    # N - 2N의 범위안 소수 개수 세기
    cnt = 0
    for num in range(N+1, 2*N +1):
        if is_prime[num]:
            cnt += 1

    print(cnt)
