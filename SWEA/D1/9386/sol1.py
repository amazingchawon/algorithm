# [D1] 9386 연속한 1의 개수

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())                # 수열의 길이
    numbers = input().split('0')    # 0을 기준으로 나누기

    answer = 0

    for num in numbers:
        if answer < len(num):
            answer = len(num)

    print(f'#{t} {answer}')