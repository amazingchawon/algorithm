# [D4] 5432 쇠막대기 자르기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    data = input()

    cnt = 0
    answer = 0  # 쇠막대 길이 저장할 변수

    for i in range(len(data)):
        if data[i] == '(':              # 현재 위치에서 데이터가 여는 괄호라면
            cnt += 1                    # 스택에 추가
        else:                           # 닫는 괄호이고,
            if data[i-1] == '(':        # 직전이 여는 괄호라면 -> 레이저인 경우라면
                cnt -= 1                # 레이저빼고
                answer += cnt           # 레이저 전에 있던 쇠막대 자르기
            else:                       # 쇠막대 종료지점이라면
                cnt -= 1
                answer += 1             # 쇠막대 조각 추가해주기

    print(f'#{t} {answer}')