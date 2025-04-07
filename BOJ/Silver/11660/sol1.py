# [S1] 11660 구간 합 구하기 5
# 시간 초과

N, M = map(int, input().split())                            # N : 표의 크기 M : 문제 수
arr = [list(map(int, input().split())) for _ in range(N)]   # arr : 표

for t in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0

    for dx in range(x2 - x1 + 1):
        for dy in range(y2 - y1 + 1):
            # print('x', x1 - 1 + dx, 'y', y1 - 1 + dy, '값', arr[x1 - 1 + dx][y1 - 1 + dy])
            result += arr[x1 - 1 + dx][y1 - 1 + dy]

    print(result)