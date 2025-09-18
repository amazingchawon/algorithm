# [S1] 9465 스티커
T = int(input())

for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]    # dp[i][j] : i번째 행에 j번째 스티커를 선택했을 때 최대 합

    # STEP 1. 첫번째 칸은 제약이 없으므로, 초기값 세팅
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    # STEP 2. 두번쨰 값은 첫번쨰 값에 근거하여 세팅, 대각선한 더할 수 있음
    if n > 1:
        dp[0][1] = arr[0][1] + dp[1][0]
        dp[1][1] = arr[1][1] + dp[0][0]

    # STEP 3. 두 칸 전 or 한 칸 전의 대각선 값 중 최댓값을 선택
    for j in range(2, n):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + arr[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + arr[1][j]

    print(max(dp[0][n-1], dp[1][n-1]))
