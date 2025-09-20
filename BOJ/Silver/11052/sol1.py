# [S1] 11052 카드 구매하기

# STEP 1. 변수 설정
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

# STEP 2. 초기값 세팅
dp[1] = arr[1]

# STEP 3. 점화식 계산
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[j] + arr[i-j])

# STEP 4. 출력
print(dp[-1])