# [S3] 15649 N과 M (1)

from itertools import permutations

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]        # 1-N 포함된 배열 만들기

# STEP 2. 1-N까지 자연수 중 중복 없이 M개 고르기 -> 순열
for perm in permutations(arr, M):
    print(*perm)