# [S1] 2156 포도주 시식

# STEP 1. 변수 생성
n = int(input())                        # n : 잔의 수
arr = [int(input()) for _ in range(n)]  # arr : 포도주의 양 배열

DP = [0] * n                            # DP[i] : i번째 포도주까지 최대값

# STEP 2. 계산
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    DP[0] = arr[0]
    DP[1] = arr[0] + arr[1]
    DP[2] = max(DP[1], arr[2], arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        DP[i] = max(
            DP[i-1],                        # 이번잔 안 마시는 경우
            DP[i-2] + arr[i],               # 전 잔 안 마시고, 이번잔 마시는 경우 (xo)
            DP[i-3] + arr[i-1] + arr[i]     # 전전 잔 안 마시고, 전잔 + 이번잔 마시는 경우 (xoo)
        )

    print(DP[-1])