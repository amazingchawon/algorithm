# [D3] 5188 최소합

import sys
sys.stdin = open('input.txt', 'r')

right, down = (0, 1), (1, 0)
d = [right, down]

def sum_arr(perm, used):
    global answer

    # 기저 조건
    # 순열 1개 생성 완료했다면,
    # 순열 1개 완성 길이: 배열 크기가 3*3 이라면, 우측 이동 2번, 좌측 이동 2번
    # 따라서, (N-1) * 2
    if len(perm) == (N-1) * 2:
        # STEP 2. 이동하면서 숫자 판에 적힌 숫자 더하기
        x, y = 0, 0
        tmp = arr[x][y]             # 시작칸에 적힌 숫자로 초기화
        for dx, dy in perm:
            x, y = x + dx, y + dy
            tmp += arr[x][y]
        answer = min(answer, tmp)   # answer 갱신
    # 순열 만들기
    for i in range(2):              # 우측, 아래 두가지!
        if used[i] < N-1:           # 우측 이동 (N-1)까지 가능, 좌측도 마찬가지
            perm.append(d[i])
            used[i] += 1
            sum_arr(perm, used)
            perm.pop()
            used[i] -= 1

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # STEP 1. 이동하기
    # 오른쪽으로 N번, 왼쪽으로 N번 움직여서 goal 도달하는 경우 다 탐색
    answer = 1e9
    used = [0, 0]
    sum_arr([], used)

    print(f'#{t} {answer}')