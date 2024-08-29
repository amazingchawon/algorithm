# [D2] 5186 이진수 2

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    number = float(input())     # 2진수로 바꿀 수
    x = 1/2
    answer = ''

    while number:               # number가 0이 될 동안
        if number >= x:          # number 안에 x가 들어가면
            number -= x
            answer += '1'
        else:
            answer += '0'

        x /= 2
        if len(answer) >= 13:   # 제한 조건 안에 2진수로 표현이 안되면,
            print(f'#{t} overflow')
            break
    else:
        print(f'#{t} {answer}')