# [S2] 11053 가장 긴 증가하는 부분 수열

import bisect

N = int(input())
arr = list(map(int, input().split()))

LIS = []

for num in arr:
    pos = bisect.bisect_left(LIS, num)

    if pos == len(LIS):
        LIS.append(num)
    else:
        LIS[pos] = num

print(len(LIS))