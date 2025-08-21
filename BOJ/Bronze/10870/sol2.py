# [B2] 10870 피보나치 수 5
# 파이써닉한 풀이

N = int(input())
a, b = 0, 1

for _ in range(N):
    a, b = b, a + b

print(a)