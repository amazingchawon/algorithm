# [S2] 17103 골드바흐 파티션

# STEP 1. 입력 받기
T = int(input())
N = [int(input()) for _ in range(T)]

# STEP 2. 에라토스테네스의 체로 소수 판별
is_prime = [1 for _ in range(max(N) + 1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(len(is_prime) ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, len(is_prime), i):
            is_prime[j] = 0

# STEP 3. N 순회, 골드바흐 파티션 수 구하기
for n in N:
    cnt = 0

    if is_prime[n-2]:
        cnt += 1
    if is_prime[n-3]:
        cnt += 1

    for k in range(5, n//2 + 1, 6):
        if is_prime[k] and is_prime[n - k]:
            cnt += 1
    for k in range(7, n//2 + 1, 6):
        if is_prime[k] and is_prime[n - k]:
            cnt += 1
    print(cnt)