# [S2] 18870 좌표 압축

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))
index_dict = dict(zip(sorted_arr, range(len(sorted_arr))))

for num in arr:
    print(index_dict[num], end= " ")