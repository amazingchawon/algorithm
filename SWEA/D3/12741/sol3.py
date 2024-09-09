# [D3] 12741 두 전구

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result_list = []

for t in range(1, T+1):
    # X 전구가 켜져있는 시간 : A초-B초
    # Y 전구가 켜져있는 시간 : C초-D초
    A, B, C, D = map(int, input().split())

    time = [0] * 101

    for i in range(A, B + 1):
        time[i] += 1

    for j in range(C, D + 1):
        time[j] += 1

    result = time.count(2)

    if result != 0:
        # 2, 3, 4 초에 둘다 같이 켜있었다면 -> 2초동안 같이 켜있는 것
        result -= 1

    result_list.append(result)

for index, result in enumerate(result_list):
    print(f'#{index+1} {result}')