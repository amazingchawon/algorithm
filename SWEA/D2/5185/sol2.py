# [D2] 5185 이진수

import sys
sys.stdin = open('input.txt', 'r')

hex_to_decimal = {'A': '10',
                  'B': '11',
                  'C': '12',
                  'D': '13',
                  'E': '14',
                  'F': '15'}
T = int(input())

for t in range(1, T+1):
    N, hexa = input().split()
    answer = ''

    for num in hexa:
        if num in 'ABCDEF':                 # A-F를 10-15로 변환
            num = hex_to_decimal.get(num)
        tmp =''                             # 2진수 변환한 것 넣을 변수
        for i in range(4):
            tmp += str(int(num)%2)
            num = int(num) // 2
        answer += tmp[::-1]


    print(f'#{t} {answer}')