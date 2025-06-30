# [S2] 17087 숨바꼭질 6

from math import gcd
from functools import reduce

# STEP 1. 입력 받기
N, S = map(int, input().split())
siblings = list(map(int, input().split()))

# STEP 2. 차이 구하기
diffs = [abs(x-S) for x in siblings]

# STEP 3. gcd 구하기
answer = reduce(gcd, diffs)

print(answer)