# [D3] 1240 단순 2진 암호코드

import sys
sys.stdin = open('input.txt', 'r')

decrypt = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9}

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N * M 배열
    arr = [input() for _ in range(N)]   # 1차원 배열로 입력 받기
    password = 0                        # 암호 저장 변수

    # STEP 1. arr에서 암호 코드 찾아내기
    for row in arr:                     # 암호 시작점 찾기
        for i in range(M):
            if row[i] == '1':           # 1이 들어간 문장 찾기
                password = row
                start = i               # start : 암호 시작 index
                break                   # 찾으면 바로 종료 (for i 탈출)
        if password != 0:               # 암호 찾았으면 종료 (for row 종료)
            break

    for j in range(M-1, -1, -1):        # 암호 종료점 찾기, 해당 문장 끝에서부터 순회
        if password[j] == '1':
            end = j                     # end : 암호 종료 index
            break

    length = end-start+1                # 1~1 까지 구간의 길이
    diff = 56 - length                  # 암호랑 길이 얼마나 차이나는지 찾기 (0 <= diff <= 3)
    password = '0'*diff + password[start:end+1]    # password 갱신

    # STEP 2. 해독
    result = []                         # 해독한 숫자 저장 배열
    for k in range(0, 56, 7):
        num = password[k:k+7]
        result.append(decrypt.get(num)) # 해독해서 result에 넣기

    # STEP 3. 암호 유효성 판독
    check = sum(result)                 # (홀수번째 수*3 + 짝수번째 수)의 값 저장 변수
    for m in range(0,8,2):              # 홀수번째 수만 2번 더 더해주기
        check += int(result[m]) * 2

    if check % 10 == 0:
        print(f'#{t} {sum(result)}')
    else:
        print(f'#{t} 0')
