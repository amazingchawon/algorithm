# [S2] 16493 최대 페이지 수

# STEP 1. 입력 받기
N, M = map(int, input().split())  # N: 남은 일 수, M: 챕터 수
books = [list(map(int, input().split())) for _ in range(M)]  # 각 챕터의 (소요 일수, 페이지 수) 저장

# DP 테이블 초기화: DP[m][n] → m번째 챕터까지 고려했을 때, n일 동안 읽을 수 있는 최대 페이지 수
DP = [[0] * (N+1) for _ in range(M+1)]

# STEP 2. DP 진행
for m in range(1, M+1):  # 1번 챕터부터 M번 챕터까지 순회
    for n in range(1, N+1):  # 1일부터 N일까지 순회
        if n < books[m-1][0]:  # 현재 챕터를 읽기 위한 시간이 부족하면
            DP[m][n] = DP[m-1][n]  # 이전 챕터까지 고려한 최댓값 유지
        else:  # 현재 챕터를 읽을 수 있는 경우
            # (1) 챕터를 선택하지 않는 경우: DP[m-1][n]
            # (2) 챕터를 선택하는 경우: DP[m-1][n - (소요 일수)] + (해당 챕터 페이지 수)
            DP[m][n] = max(DP[m-1][n], DP[m-1][n-books[m-1][0]] + books[m-1][1])  

# 결과 출력: N일 동안 읽을 수 있는 최대 페이지 수
print(DP[M][N])
