# [S2] 17087 숨바꼭질 6

from math import gcd

# STEP 1. 입력 받기
N, S = map(int, input().split())
siblings = list(map(int, input().split()))

# STEP 2. 동생들, 수빈이 거리 차이 구하기
siblings.append(S)
siblings.sort()

diffs = []

for i in range(N):
    diffs.append(siblings[i+1] - siblings[i])

# STEP 3. gcd 구하기
answer = diffs[0]
for j in range(1, N):
    answer = gcd(answer, diffs[j])

print(answer)