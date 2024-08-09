# [D4] 1223 계산기 2

import sys
sys.stdin = open('input.txt', 'r')

# priority dict
priority = {'*' : 2,'+' : 1}

for t in range(1, 11):
    N = int(input())    # 중위 표기식 길이
    infix = input()     # 변환해야하는 중위 표기식

    postfix = ''        # 후위 표기식으로 변환해서 저장할 변수
    operator = []       # 연산자 저장 스택
    top = -1            # 연산자 스택 top 위치 저장 변수

    # 중위 표기식 -> 후위 표기식 변환
    for char in infix:
        if char.isdecimal():    # 숫자라면
            postfix += char     # 후위 표기식에 넣기
        else:                   # 연산자라면
            while True:
                if top > -1 and priority[operator[top]] >= priority[char]:
                    postfix += operator.pop()
                    top -= 1
                else:
                    operator.append(char)
                    top += 1
                    break
    while top > -1:
        postfix += operator.pop()
        top -= 1

    # 수식 계산
    operand = []    # 피연산자를 담을 스택
    top = -1        # operand 스택 top 위치를 기록할 변수

    for char in postfix:
        if char.isdecimal():    # 피연산자라면,
            operand.append(char)
        else:
            right = int(operand.pop())
            left = int(operand.pop())
            if char == '+':
                operand.append(left + right)
            elif char == '*':
                operand.append(left * right)

    answer = operand.pop()
    print(f'#{t} {answer}')