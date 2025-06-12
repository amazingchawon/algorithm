# [B1] 11653 소인수분해

# STEP 1. 입력 받기
N = int(input())

# STEP 2. N까지 소수 찾기 (유크리드 호제법)
is_prime = [1 for _ in range(N+1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*2, N+1, i):
            is_prime[j] = 0

# STEP 3. N 약분하기
answer = []                             # N의 약수를 기록할 배열

for num in range(2, len(is_prime)):
    if is_prime[num]:                   # 소수면,
        while N % num == 0:             # N을 소수로 나누기 (해당 소수로 안 나눠떨어질때까지)
            N = N//num                  # N 갱신
            answer.append(num)          # answer에 약수 추가
    if N == 1:                          # N이 1이면 약수 찾기 종료
        break

for divisor in answer:
    print(divisor)