# [D3] 2805 농작물 수확하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # mid : 가운데 줄 인덱스, answer : 수익 저장 변수
    mid = N//2
    # 초기값 = 중간줄(가로 기준)의 수익
    answer = sum(farm[mid])

    # 가운데 줄에서 한 줄 씩 위/아래로 올라/내려가서 수익 더해주기
    for i in range(1, mid + 1):
        # mid - i : 가운데에서 i번쨰 위 줄
        # i : N-i : 앞에서 i번째 인덱스 - 뒤에서 i번째 인덱스까지 더해주기
        answer += sum(farm[mid - i][i:N-i])
        answer += sum(farm[mid + i][i:N-i])

    print(f'#{t} {answer}')