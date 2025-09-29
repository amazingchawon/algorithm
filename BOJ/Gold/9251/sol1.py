# [G5] 9251 LCS

# STEP 1. 변수 할당
s1 = input().strip()
s2 = input().strip()

DP = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]    # DP[x][y] : s1의 x까지랑 s2의 y까지의 LCS 최대 값

# STEP 2. LCS 찾기
for x in range(1, len(s1) + 1):
    for y in range(1, len(s2) + 1):
        if s1[x-1] == s2[y-1]:
            DP[x][y] = DP[x-1][y-1] + 1
        else:
            DP[x][y] = max(DP[x-1][y], DP[x][y-1])

print(DP[len(s1)][len(s2)])