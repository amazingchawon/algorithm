# [B2] 1978 소수 찾기

# STEP 1. 입력 받기
N = int(input())
arr = list(map(int, input().split()))

# STEP 2. 에라토스테네스의 체 적용
is_prime = [1 for _ in range(1001)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(1000**0.5)+1):
    if is_prime[i]:
        for j in range(i*2, 1001, i):
            is_prime[j] = 0

#STEP 3. arr 안에 소수 개수 세기
answer = 0
for num in arr:
    if is_prime[num]:
        answer += 1

print(answer)