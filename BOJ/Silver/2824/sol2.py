# [S1] 2824 최대 공약수

from collections import Counter

# STEP 0. 소인수분해 함수 구현
# 숫자 n을 소인수분해하여 counter 딕셔너리에 소인수의 개수를 누적
def prime_factors(counter, n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            counter[i] += 1
            n //= i
        i += 1
    # n이 소수인 채로 남은 경우 (ex: 13 등)
    if n > 1:
        counter[n] += 1

# STEP 1. 입력 받기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# STEP 2. 각 숫자들을 소인수분해하여 개수를 카운트
A_counter = Counter()
B_counter = Counter()

for a in A:
    prime_factors(A_counter, a)

for b in B:
    prime_factors(B_counter, b)

# STEP 3. A와 B에서 공통으로 등장한 소인수들만 골라,
# 각 소인수의 개수 중 더 적은 만큼 곱해서 GCD를 구함
answer = 1
overflow = False  # 결과가 10억 이상이면 출력 방식이 달라지므로 추적

for factor in A_counter:
    if factor in B_counter:
        # 공통된 소인수일 경우, 등장 횟수 중 최소값만큼 곱함
        for _ in range(min(A_counter[factor], B_counter[factor])):
            answer *= factor
            # 10억 이상이 되면 뒤 9자리만 남기고 overflow 표시
            if answer >= 10**9:
                answer %= 10**9
                overflow = True

# STEP 4. 출력: 10억 이상이면 앞에 0을 붙여 9자리 문자열 출력
if overflow:
    print(str(answer).zfill(9))  # 앞자리 0을 붙여 9자리 유지
else:
    print(answer)  # 10억 미만이면 그대로 출력