# [D2] 1979 어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1) :
    # N : 퍼즐의 가로, 세로 길이 (5 <= N <= 15)
    # K : 단어의 길이 (2 <= K <= N)
    N , K = map(int, input().split())

    # 퍼즐 2차원 배열 생성
    puzzle = [list(map(str, input().split())) for _ in range(N)]

    # 정답 변수
    answer = 0

    # 가로 탐색
    # 1(흰색 칸)이 연달아 몇개 있는지 체크
    for row in puzzle :
        # 00110111 이런식의 자료를 ['', '', '11', '', '111'] 이렇게 1만 볼 수 있게 변환
        temp = ''.join(row).split('0')
        for i in temp :
            if len(i) == K :
                answer += 1

    # 세로 탐색
    for i in range(N) :
        # 세로 값을 저장할 빈 문자열
        col = ''
        # 가로 줄에서 해당하는 세로 값 추가
        for row in puzzle :
            col += row[i]

        temp = ''.join(col).split('0')
        for i in temp :
            if len(i) == K :
                answer += 1

    # 정답 출력 (형식 : # 테스트케이스 정답)
    print(f'#{t} {answer}')