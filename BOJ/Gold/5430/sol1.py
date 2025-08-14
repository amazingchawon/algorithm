# [G5] 5430 AC
# 시간 초과

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    tmp = input().strip()[1:-1]
    x = deque(list(map(int, tmp.split(',')))) if n > 0 else deque([])

    for func in p:
        if func == 'R':
            x.reverse()
        else:
            if len(x) > 0:
                x.popleft()
            else:
                print('error')
                break
    else:
        print(list(x))