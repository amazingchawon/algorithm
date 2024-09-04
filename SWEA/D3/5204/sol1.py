# [D3] 5204 병합정렬

import sys
sys.stdin = open('input.txt', 'r')


def merge_sort(m):
    if len(m) == 1:
        return m

    mid = len(m)//2
    l = m[:mid]
    r = m[mid:]

    left = merge_sort(l)
    right = merge_sort(r)

    return merge(left, right)


def merge(left, right):
    result = [0] * (len(left) + len(right))
    l, r = -1, -1     # l, r : left, right 인덱스 접근을 위한 변수
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    while l >= -len(left) and r >= -len(right):
        if left[l] > right[r]:          # 문제 조건! 왼쪽의 마지막 원소가 오른쪽 마지막 원소보다 클 경우
            result[l+r+1] = left[l]     # 전체 배열의 뒤부터 채우기
            l -= 1                      # l 인덱스 갱신
        else:
            result[l+r+1] = right[r]
            r -= 1

    while l >= -len(left):
        result[l+r+1] = left[l]
        l -= 1

    while r >= -len(right):
        result[l+r+1] = right[r]
        r -= 1

    return result


T = int(input())

for t in range(1, T+1):
    N = int(input())                        # 정렬하고자 하는 배열 길이
    arr = list(map(int, input().split()))   # 정렬하고자 하는 배열
    cnt = 0                                 # 문제 조건을 달성한 횟수 저장 변수

    arr = merge_sort(arr)

    print(f'#{t} {arr[N//2]} {cnt}')