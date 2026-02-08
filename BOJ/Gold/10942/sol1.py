# [G4] 10942 팰린드롬?
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# STEP 1. 입력 받기
N = int(input())
arr = list(map(int, input().split()))

M = int(input())

# STEP 2. DP
dp = [[-1] * N for _ in range(N)]  # dp[s][e]: s번째 수부터 e번째까지의 수가 팰린드롬이면 1

# STEP 2.1. 전처리
for i in range(N):
    dp[i][i] = 1
    if i + 1 < N and arr[i] == arr[i + 1]:
        dp[i][i+1] = 1

# STEP 2.3. 함수 정의
def is_palin(s, e):
    # 종료 조건
    if s >= e:
        return 1

    if arr[s] != arr[e]:
        dp[s][e] = 0
        return 0

    if dp[s][e] != -1:
        return dp[s][e]

    tmp = is_palin(s + 1, e - 1)
    dp[s][e] = tmp
    return tmp

for _ in range(M):
    s, e = map(int, input().split())
    s, e = s - 1, e - 1

    is_palin(s, e)
    print(dp[s][e])
