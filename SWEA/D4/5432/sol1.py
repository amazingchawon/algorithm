# [D4] 5432 쇠막대기 자르기

# 런타임 에러

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    data = input().split('()')  # 레이저로 나누기
    data = '0'.join(data)       # 레이저 0으로 표시

    stack = []      # 여는 괄호[(] 인덱스를 저장할 스택
    pipes = []      # [[쇠막대기 1 시작 인덱스, 끝 인덱스], ..]
    lasers = []     # [레이저 1 인덱스, 레이저 2 인덱스 ..]

    answer = 0      # 쇠막대기 개수 저장할 변수

    # 쇠막대기, 레이저 위치 기록
    for i in range(len(data)):
        if data[i] == '0':                  # 레이저라면,
            lasers.append(i)                # 레이저 리스트에 추가
        elif data[i] == '(':                # 여는 괄호라면,
            stack.append(i)                 # 여는 괄호 인덱스 추가
        else:                               # 닫는 괄호라면,
            pipes.append([stack.pop(), i])  # [쇠막대기 시작 인덱스, 끝 인덱스] 추가

    # 쇠막대기 절단
    for pipe in pipes:
        cnt = 1                             # 쇠막대기 개수
        for laser in lasers:
            if pipe[0] < laser < pipe[1]:   # 현재 쇠막대기 위치 안에 있는 레이저라면,
                cnt += 1
        answer += cnt                       # 쇠막대기 개수 추가

    print(f'#{t} {answer}')