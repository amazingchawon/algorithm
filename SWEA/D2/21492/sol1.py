# [D2] 21492 색칠하기

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())                    # 색칠할 횟수
    arr = [[0]*10 for _ in range(10)]   # 10*10 격자

    answer = 0

    # 색칠하기
    for i in range(N):
        x1, y1, x2, y2, c = list(map(int, input().split())) # xi, yi : 색칠 시작/끝 좌표, c : 색깔

        for dx in range(x2-x1+1):               # 색칠할 사각형의 세로 길이
            for dy in range(y2-y1+1):           # 색칠할 사각형의 가로 길이
                arr[x1 + dx][y1 + dy] += c      # 색칠

    # 겹쳐진 부분 찾기 (겹쳐진 부분 -> arr에서 3으로 표시되어있는 부분
    for row in arr:
        answer += row.count(3)

    print(f'#{t} {answer}')