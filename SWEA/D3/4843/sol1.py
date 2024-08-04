# 4843 특별한 정렬

import sys
sys.stdin = open('input.txt', 'r')

def find_max(arr):
    max_num = arr[0]

    for num in arr:
        if max_num < num:
            max_num = num
    
    return max_num

def counting_sort(arr, N):
    tmp = [0] * (find_max(arr)+1)   # 입력받은 배열의 원소 등장 횟수를 기록할 배열 생성

    # 원소 등장횟수 기록
    for i in arr:
        tmp[i] += 1

    # 원소 등장횟수 누적합
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i-1]
    
    # 새로운 배열에 tmp 사용해서 정렬
    arr = arr[::-1] # 안정정렬을 만들기 위해 정렬 순서 뒤바꾸기
    sorted_arr = [-1] * N

    for num in arr:
        tmp[num] -= 1
        sorted_arr[tmp[num]] = num

    return sorted_arr

T = int(input())  # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input())    # 정수의 개수
    arr = list(map(int, input().split()))   # 정렬할 배열 받기

    # 1. 입력받은 배열 정렬 -> 카운팅 정렬 사용
    arr = counting_sort(arr, N)

    # 2. 특별한 정렬로 정렬
    special_sorted_arr = [-1] * N
    
    # 큰수 -> 작은수를 짝수 인덱스에 배치
    idx = N-1
    # 큰수
    for i in range(0, N, 2):
        special_sorted_arr[i] = arr[idx]
        idx -= 1

    # 작은수
    if N % 2 == 0:  # N이 짝수일 때 -> 끝 칸부터 채워넣기
        for i in range(N-1, 0, -2):
            special_sorted_arr[i] = arr[idx]
            idx -=1
    else:   # N이 홀수일 때 -> 끝에서 한 칸 앞에서부터 채워넣기
        for i in range(N-2, 0, -2):
            special_sorted_arr[i] = arr[idx]
            idx -= 1

    
    print(f'#{t}', end=' ')
    for i in range(10):
        print(special_sorted_arr[i], end=' ')
    print()