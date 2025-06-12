# [B1] 2609 최대공약수와 최소공배수

from math import gcd
# STEP 1. 입력 받기
N, M = map(int, input().split())

# STEP 2. 최대 공약수 구하기
k = gcd(N, M)
print(k)

# STEP 3. 최소 공배수 구하기
print((N*M)//k)