# [G5] 5430 AC

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    tmp = input().strip()[1:-1]
    x = deque(list(map(int, tmp.split(',')))) if n > 0 else deque([])

    front = True

    for func in p:
        if func == 'R':
            front = not front
        else:
            if len(x) > 0:
                if front:
                    x.popleft()
                else:
                    x.pop()
            else:
                print('error')
                break
    else:
        if not front:
            x.reverse()
        print('[' + ','.join(map(str, x)) + ']')