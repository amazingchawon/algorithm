# [D3] 5658 보물상자 비밀번호

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())    # N : 숫자 총 길이, K : 숫자 조합 중 K번째로 큰 수가 정답
    arr = list(input())                 # arr : 보물 상자 숫자 저장 배열

    times = N//4                # times 만큼 회전, 그 다음 회전부터는 같은 값이 나옴
    numbers = set()             # 숫자 저장 집합, 중복 숫자 제거를 위해 집합으로 생성

    # STEP 1. 모든 수 조합 구하기
    for time in range(times):
        for i in range(0, N, times):                            # times 길이만큼 숫자를 나눠봐야함
            # arr[i:i+times] : times 길이만큼 arr 자르기
            # join : 리스트 str으로 변환
            # int(str, 16) : str -> 16진수로 인식 -> 2진수 변환
            numbers.add(int(''.join(arr[i:i+times]), 16))       # 숫자 저장

        arr = [arr.pop()] + arr                                 # 회전하고 한 칸 이동해서 배열에 저장

    # STEP 2. K번째로 큰 수 구하기
    num_lst = sorted(list(numbers), reverse=True)

    print(f'#{t} {num_lst[K-1]}')