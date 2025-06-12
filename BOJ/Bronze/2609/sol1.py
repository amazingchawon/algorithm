# [B1] 2609 최대공약수와 최소공배수

# STEP 0. 유쿨리드 호제법으로 gcd 구하는 함수 구현
def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# STEP 1. 입력 받기
N, M = map(int, input().split())

# STEP 2. 최대 공약수 구하기
gcd = get_gcd(N, M)
print(gcd)

# STEP 3. 최소 공배수 구하기
lcm = (N * M) // gcd

print(lcm)