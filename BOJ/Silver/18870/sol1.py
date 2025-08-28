# [S2] 18870 좌표 압축

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

index_dict = {}

sorted_arr = sorted(list(set(arr)))
cnt = 0

for num in sorted_arr:
    index_dict[num] = cnt
    cnt += 1

result = []

for num in arr:
    result.append(index_dict[num])

print(*result)