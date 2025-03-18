# [G5] 12865 평범한 배낭

# STEP 1. 입력 받기
N, K = map(int, input().split())  # N: 물품 수, K : 최대 무게
items = [list(map(int, input().split())) for _ in range(N)] # 각 물건의 (W: 무게, V: 가치) 저장

# DP 테이블 초기화: DP[i][w] -> i번째 아이템까지 고려했을 때 w까지 무게를 채웠을 때 최대 효용
DP = [[0] * (K+1) for _ in range(N+1)]

# STEP 2. DP 진행
for i in range(1, N+1): # 아이템 순회
    for k in range(1, K+1): # 무게 순회
        if k < items[i-1][0]: # 현재 아이템을 담기 위해 용량이 부족하면
            DP[i][k] = DP[i-1][k]
        else:  # 현재 아이템 넣을 수 있는 경우
            # (1) 아이템을 선택하지 않는 경우: DP[i-1][k]
            # (2) 아이템을 선택하는 경우: DP[i-1][n - (무게)] + (해당 아이템 가치)
            DP[i][k] = max(DP[i-1][k], DP[i-1][k-items[i-1][0]] + items[i-1][1])

print(DP[N][K])
