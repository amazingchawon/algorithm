# [D3] 1289 원재의 메모리 복구하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # original : 원래 값, answer : 수정 횟수
    orginal = input()
    answer = 0

    # curr : 현재 메모리 값
    curr = '0' * len(orginal)

    for i in range(len(orginal)):
        # 현재 i번째 값이 원본과 다를 때
        if curr[i] != orginal[i]:
            # curr의 i번째 값부터 끝까지 original[i] 값으로 바꾸기
            curr = curr[0:i] + orginal[i]*(len(orginal)-i)
            answer += 1

    print(f'#{t} {answer}')