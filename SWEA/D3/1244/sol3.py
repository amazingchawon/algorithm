# [D3] 1244 최대 상금

import sys
sys.stdin  = open('input.txt', 'r')

def perm(level):
    global answer
    if level == time:               # time번 교환했을때
        tmp = int(''.join(num))     # tmp : num 숫자로 바꿔서 저장
        if answer < tmp:            # answer보다 tmp가 더 크다면 갱신
            answer = tmp
        return

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]

            tmp = ''.join(num)
            if (tmp, level) in visited:  # 똑같은 결과가 이미 저장되어 있다면 pass
                pass
            else:
                visited.add((tmp, level))  # 없다면 기록해두기
                perm(level+1)

            num[i], num[j] = num[j], num[i]



T = int(input())

for t in range(1, T+1):
    num, time = input().split()     # num : 숫자판 정보, time : 교환 횟수
    answer = 0          # time만큼 교환했을때 가장 큰 수 기록하는 변수
    num = list(num)     # 숫자판 정보 list로 변환
    time = int(time)    # 교환 횟수
    visited = set()     # 0 <-> 1, 1 <-> 0 이든 상관 X, 몇번째 차례에 어디어디를 교환했는지 기록하는 배열

    perm(0)

    print(f'#{t} {answer}')