# [G5] 5557 1학년

# STEP 1. 입력받기
N = int(input())
numbers = list(map(int, input().split()))

# STEP 2. DP
dp = [[0] * 21 for _ in range(N)]   # dp[x][y] : numbers의 x 번째까지 계산했을때 결과값 y
dp[0][numbers[0]] = 1               # 첫번째 숫자 기록

for i in range(N-2):
    for j in range(21):
        if dp[i][j]:
            add = j + numbers[i+1]  # i 번째 수까지 계산한 결과값 y + 현재 숫자
            minus = j - numbers[i+1]    # i 번째 수까지 계산한 결과값 y  - 현재 숫자
            if add <= 20:
                dp[i+1][add] += dp[i][j]
            if minus >= 0:
                dp[i+1][minus] += dp[i][j]

print(dp[N-2][numbers[-1]])