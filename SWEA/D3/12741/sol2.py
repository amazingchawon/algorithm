# [D3] 12741 두 전구

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result_list = []

for t in range(1, T+1):
    # X 전구가 켜져있는 시간 : A초-B초
    # Y 전구가 켜져있는 시간 : C초-D초
    A, B, C, D = map(int, input().split())

    # case 1. A B C D
    if B < C:
        result = 0
    # case 2. A C B D
    elif A <= C <= B <= D:
        result = B - C
    # case 3. C A B D
    elif C <= A and B <= D:
        result = B - A
    # case 4. C A D B
    elif C <= A <= D <= B:
        result = D - A
    # case 5. A C D B:
    elif A <= C and D <= B:
        result = D - C
    # case 6. C D A B
    elif D <= A:
        result = 0

    result_list.append(result)

for index, result in enumerate(result_list):
    print(f'#{index+1} {result}')