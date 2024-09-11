# [D4] 5247 연산

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque


def calculate(cal, num):
    '''
    :param cal: 연산 타입
    :param num: 연산할 숫자
    :return: 연산 결과
    '''
    if cal == 0:
        return num + 1
    elif cal == 1:
        return num - 1
    elif cal == 2:
        return num * 2
    else:
        return num - 10


def min_cal(num, target):
    # visited : 연산결과 저장하는 집합, 이미 연산해본 숫자라면 다시 연산할 필요 없음 (이전에 연산한게 횟수가 더 적을테니까)
    visited = set([num])
    q = deque()
    q.append((num, 0))

    while q:
        curr, level = q.popleft()
        if curr == target:
            return level
        for i in range(4):
            tmp = calculate(i, curr)
            # 범위 체크
            if tmp not in visited and -1 <= tmp <= 1000000:
                q.append((tmp, level + 1))
                visited.add(tmp)


T = int(input())

for t in range(1, T+1):
    # N: 현재 숫자, M: 만들고자 하는 숫자
    N, M = map(int, input().split())

    answer = min_cal(N, M)

    print(f'#{t} {answer}')