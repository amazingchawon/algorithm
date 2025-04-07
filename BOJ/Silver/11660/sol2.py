# [S1] 11660 구간 합 구하기 5

# STEP 1. 입력 받기
N, M = map(int, input().split())                            # N : 표의 크기 M : 문제 수
arr = [list(map(int, input().split())) for _ in range(N)]   # arr : 표

S = [[0] * N for _ in range(N)]

# STEP 2. 누적합 배열 만들기
for x in range(N):
    for y in range(N):
        S[x][y] = arr[x][y]
        if x > 0:
            S[x][y] += S[x-1][y]
        if y > 0:
            S[x][y] += S[x][y-1]
        if x > 0 and y > 0:
            S[x][y] -= S[x-1][y-1]

# STEP 3. 구간합 구하기
for t in range(M):
    x1, y1, x2, y2 = [v - 1 for v in map(int, input().split())]

    result = S[x2][y2]

    if x1 > 0:
        result -= S[x1-1][y2]
    if y1 > 0:
        result -= S[x2][y1-1]
    if x1 > 0 and y1 > 0:
        result += S[x1-1][y1-1]

    print(result)