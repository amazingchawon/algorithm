# [S4] 18258 큐2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    prompt = input().strip()

    if prompt.startswith('push'):
        _, num = prompt.split()
        q.append(num)
    elif prompt == 'pop':
        print(q.popleft() if q else -1)
    elif prompt == 'size':
        print(len(q))
    elif prompt == 'empty':
        print(0 if q else 1)
    elif prompt == 'front':
        print(q[0] if q else -1)
    elif prompt == 'back':
        print(q[-1] if q else -1)
