# [D1] 9367 점점 커지는 당근의 개수

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input()) # 당근의 수
    carrots = list(map(int, input().split()))   # 당근 크기 기록 배열

    answer = 1  # 최대 연속 증가 당근 수 기록 변수 (출력할 변수)
    cnt = 1     # 연속으로 커지는 당근 수 기록 변수

    for i in range(1, N):               # carrots 순회
        if carrots[i-1] < carrots[i]:   # 직전 당근보다 크다면,
            cnt += 1                    # 기록 증가
        else:
            if answer < cnt:            # 최대 연속 증가 당근 수보다 현재 기록이 더 클 경우
                answer = cnt            # 갱신
            cnt = 1                     # cnt 초기화

    if answer < cnt:
        answer = cnt

    print(f'#{t} {answer}')