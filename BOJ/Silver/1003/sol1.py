# [S3] 1003 피보나치 함수

import sys
input = sys.stdin.readline

fibo_count = [(1, 0), (0, 1)] + [None] * 39

for i in range(2, 41):
    zero = fibo_count[i-1][0] + fibo_count[i-2][0]
    one = fibo_count[i-1][1] + fibo_count[i-2][1]
    fibo_count[i] = (zero, one)

T = int(input())

for _ in range(T):
    N = int(input())

    print(*fibo_count[N])