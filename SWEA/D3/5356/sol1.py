# [D3] 5356 의석이의 세로로 말해요

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # 의석이가 만든 단어 5개를 담은 2차원 배열
    # 각 단어는 글자 하나씩 분리해서 리스트 형태로 저장
    arr = [list(input()) for _ in range(5)]

    max_length = len(arr[0])    # 5개의 단어 중 가장 긴 단어의 길이를 담을 변수

    for word in arr:            # arr 순회, 긴 단어 찾기
        if max_length < len(word):
            max_length = len(word)

    answer = ''

    for i in range(max_length): # 가장 긴 단어 기준,
        tmp = ''                # 현재 열에 있는 글자를 저장할 변수
        for j in range(5):
            row = arr[j]
            if len(row) >= i +1:    # 현재 행에 i번째 글자가 존재하는지 범위 체크
                tmp += row[i]       # tmp 갱신
        answer += tmp               # answer 갱신

    print(f'#{t} {answer}')