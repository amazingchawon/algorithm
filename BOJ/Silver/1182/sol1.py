# [S2] 1182 부분수열의 합

from itertools import combinations

# STEP 1. 입력 받기
N, S = map(int, input().split())        # N : arr의 길이, S : 요구하는 부분 수열의 합
arr = list(map(int, input().split()))

answer = 0

# STEP 2. 길이가 1 ~ N인 부분 수열 찾기
for i in range(1, N + 1):
    for combi in combinations(arr, i):
        if sum(combi) == S:
            answer += 1

print(answer)