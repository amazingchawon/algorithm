# [D2] 4839 이진탐색

import sys
sys.stdin = open('input.txt', 'r')

def binary_search_cnt(left, right, center, target):
    cnt = 0
    while center != target:                 # 찾는 쪽 번호가 중간 페이지와 같아질때까지 반복
        center = int((left + right) / 2)
        if target > center:                 # 타겟이 중간 페이지보다 크면
            left = center                   # 중간 페이지 뒤 탐색
        else:                               # 타켓이 중간 페이지보다 작으면
            right = center                  # 중간 페이지 앞 탐색
        cnt += 1
    return cnt

T = int(input())

for t in range(1, T+1):
    # P : 전체 쪽수
    # A, B : A, B가 찾을 쪽 번호
    P, A, B = map(int, input().split())

    a = binary_search_cnt(1, P, int((1+P)/2), A)
    b = binary_search_cnt(1, P, int((1+P)/2), B)

    if a < b:               # A가 탐색을 적게 했다면
        print(f'#{t} A')    # A가 출력
    elif b < a:
        print(f'#{t} B')
    else:                   # 둘의 탐색 횟수가 동일하다면
        print(f'#{t} 0')    # 0 출력
