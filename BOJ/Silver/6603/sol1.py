# [S2] 6603 로또
from itertools import combinations

while True:
    tc = list(map(int, input().split()))

    # 끝나는 조건
    if tc[0] == 0:
        break

    # STEP 1. 입력 받기
    k, *S = tc          # k: 집합 S의 크기, S: 1-49 중 k개의 숫자가 담겨있는 집합

    # STEP 2. 조합 출력
    for combi in list(combinations(S, 6)):
        for num in combi:
            print(num, end=" ")
        print()

    print()