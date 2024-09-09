# [D3] 12741 두 전구

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result_list = []

for t in range(1, T+1):
    # X 전구가 켜져있는 시간 : A초-B초
    # Y 전구가 켜져있는 시간 : C초-D초
    A, B, C, D = map(int, input().split())

    start = max(A, C)
    end = min(B, D)

    result = end - start
    if result <= 0:     # 안겹치는 경우
        result = 0

    result_list.append(result)

for index, result in enumerate(result_list):
    print(f'#{index+1} {result}')