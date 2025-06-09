# [S2] 9020 골드바흐의 추측

# STEP 0. 10000보다 작은 모든 소수 찾기 (에라토스테네스의 체)
is_prime = [1 for _ in range(10001)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(10001**0.5)):
    if is_prime[i]:                         # i가 소수라면
        for j in range(i+i, 10001, i):      # i의 배수를
            is_prime[j] = 0                 # 모두 지워주기

# STEP 1. 입력 받기
T = int(input())

for _ in range(T):
    N = int(input())

    # STEP 2. 골드바흐 파티션 찾기
    k = N//2
    while True:
        if is_prime[k] and is_prime[N-k]:   # k와 N-k가 모두 소수라면,
            print(k, N-k)                   # 골드바흐 파티션 발견!
            break
        else:
            k -= 1                          # k 하나씩 줄여서 반복