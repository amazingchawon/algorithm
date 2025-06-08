# [G4] 2110 공유기 설치
# 완전 탐색, 시간 초과

from itertools import combinations
from math import inf

# STEP 1. 입력 받기
N, C = map(int, input().split())    # N : 집 개수, C : 공유기 개수
homes = sorted(list(int(input()) for _ in range(N)))    # homes : 집 오름차순으로 정렬한 배열

answer = 0                          # answer : 가장 인접한 두 공유기 사이 거리의 최대값을 저장할 변수

# STEP 2. C개의 집 묶기
for combi in combinations(homes, C):
    # STEP 3. 해당 집 묶음에서 가장 인접한 두 공유기 사이의 거리 구하기
    tmp = inf
    for i in range(C-1):
        tmp = min(combi[i+1]-combi[i], tmp)
    answer = max(tmp, answer)

print(answer)
