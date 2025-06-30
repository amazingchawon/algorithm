# [S1] 2824 최대 공약수
# 실페, 에라토스테네스의 체 범위 오버

# STEP 1. 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# STEP 2. 에라토스테네스의 체
length = max(max(A), max(B))
is_prime = [1 for _ in range(length + 1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(len(is_prime)**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, len(is_prime), i):
            is_prime[j] = 0

# STEP 3. A 순회, 소인수분해
a_measure = [0] * (length + 1)
gcd = [0] * (length + 1)

for a in A:
    while a > 1:
        if is_prime[a]:
            a_measure[a] += 1
            a = 1
        else:
            for i in range(1, int(a**0.5) + 1):
                if is_prime[i] and a % i == 0:
                    a //= i
                    a_measure[i] += 1

# STEP 4. B 순회, 소인수분해
for b in B:
    while b > 1:
        if is_prime[b]:
            if a_measure[b] and gcd[b] < a_measure[b]:
                gcd[b] += 1
            b = 1
        else:
            for i in range(2, int(b**0.5) + 1):
                if is_prime[i] and b % i == 0:
                    b //= i
                    if a_measure[i] and gcd[i] < a_measure[i]:
                            gcd[i] += 1

# STEP 5. gcd 순회
answer = 1
overflow = False

for i in range(len(gcd)):
    if gcd[i]:
        for _ in range(gcd[i]):
            answer *= i
            if answer >= 10**9:
                overflow = True
                answer %= 10**9

if overflow:
    print(str(answer).zfill(9))
else:
    print(answer)
