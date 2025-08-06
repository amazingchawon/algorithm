# [S4] 10866 덱

from collections import deque
import sys
input = sys.stdin.readline

# STEP 1. 변수 할당
N = int(input())
deq = deque()

for _ in range(N):
    command = input().strip()

    if command.startswith('push_front'):
        _, num = command.split()
        deq.appendleft(num)
    elif command.startswith('push_back'):
        _, num = command.split()
        deq.append(num)
    elif command == 'pop_front':
        print(deq.popleft()) if len(deq) else print(-1)
    elif command == 'pop_back':
        print(deq.pop()) if len(deq) else print(-1)
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        print(0) if len(deq) else print(1)
    elif command == 'front':
        print(deq[0]) if len(deq) else print(-1)
    elif command == 'back':
        print(deq[-1]) if len(deq) else print(-1)