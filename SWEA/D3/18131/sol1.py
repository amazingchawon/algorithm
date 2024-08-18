# [D3] 18131 부분집합의 합

import sys
sys.stdin = open('input.txt', 'r')

def subset_sum_zero(arr):
    # 부분집합 만들기
    subsets = [[]]

    for num in arr:                             # arr 원소 순회
        for i in range(len(subsets)):           # subset의 길이만큼 반복
            subsets += [subsets[i]+[num]]       # 현재 subset의 원소에 arr의 원소를 추가한 리스트를 추가

    subsets.pop(0)                              # 공집합 제거용

    for subset in subsets:                      # 부분집합 순회
        sum = 0                                 # 부분집합의 합 저장 변수
        for num in subset:                      # 부분집합 1개 순회
            sum += num                          # 더해주기
        if sum == 0:                            # 다 더하고 0이면,
            return 1                            # 1 리턴

    return 0                                    # 없다면, 0 리턴


T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))

    print(f'#{t} {subset_sum_zero(arr)}')
