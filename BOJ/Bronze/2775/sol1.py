# [B1] 2775 부녀회장이 될테야

def solve():
    # 테스트 케이스 개수
    T = int(input())

    # 모든 가능한 경우를 계산하기 위해 DP 테이블 초기화
    dp = [[0] * 15 for _ in range(15)]  # 최대 14층, 14호까지 필요

    # 0층 초기화 (1호 ~ 14호까지)
    for i in range(1, 15):
        dp[0][i] = i

    # DP 채우기 (1층부터 14층까지)
    for floor in range(1, 15):
        for room in range(1, 15):
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]

    # 입력값에 따라 정답 출력
    for _ in range(T):
        x = int(input())  # 층
        y = int(input())  # 호
        print(dp[x][y])

solve()
