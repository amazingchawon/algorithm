# [D2] 4874 Forth

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    postfix = input().split()     # 변환해야하는 중위 표기식

    operand = []    # 피연산자를 담을 스택
    answer = 0

    for char in postfix:
        if char.isdecimal():        # 피연산자라면,
            operand.append(char)
        elif char == '.':           # . 이라면,
            break
        else:                       # 연산자라면,
            if len(operand) < 2:    # 피연산자 stack 길이가 2보다 짧을 떄
                answer = 'error'    # 오류
                break
            else:
                right = int(operand.pop())
                left = int(operand.pop())
                if char == '+':
                    operand.append(left + right)
                elif char == '-':
                    operand.append(left - right)
                elif char == '/':
                    operand.append(left // right)
                elif char == '*':
                    operand.append(left * right)

    if answer != 'error' and len(operand) == 1: # 정상적으로 계산이 된다면 (answer 가 error로 갱신이 안되었고 + 스택에 연산의 결과만 남아있다면)
        answer = operand.pop()
    else:
        answer = 'error'

    print(f'#{t} {answer}')

