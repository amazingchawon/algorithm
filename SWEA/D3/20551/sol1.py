# [D3] 20551 증가하는 사탕 수열

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # 사탕의 수
    a, b, c = map(int, input().split())

    answer = 0

    # a < b < c 로 만들어주기 위해 사탕 먹기
    if c <= b :
        answer += b - c + 1
        b = c - 1
    if b <= a :
        answer += a - b + 1
        a = b - 1

    # 음수가 나오거나 모든 사탕을 다 먹어야 된다면,
    if a <= 0 or b <= 0 or c <= 0:
        answer = -1

    print(f'#{t} {answer}')