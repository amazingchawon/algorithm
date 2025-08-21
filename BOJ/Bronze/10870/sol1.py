# [B2] 10870 피보나치 수 5
# 재귀, 메모이제이션 사용

N = int(input())
memo = [-1] * (N+1)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    else:
        return fibo(n-2) + fibo(n-1)

print(fibo(N))