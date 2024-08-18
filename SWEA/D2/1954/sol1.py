# [D2] 1954 달팽이 숫자

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]     # 2차원 배열 생성
    num = 2                             # 넣어줄 숫자
    x, y = 0, 0                         # arr 인덱스
    arr[x][y] = 1                       # 숫자 넣기

    while num <= N*N:                   # 0 ~ N*N 까지 숫자를 기록
        # 델타 탐색, 우 하 좌 상
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            while 0 <= x + dx < N and 0 <= y + dy < N and arr[x + dx][y + dy] == 0:     # 범위 안이고, 비어있다면,
                x, y = x + dx, y + dy                                                   # x, y 갱신
                arr[x][y] = num
                num += 1

    print(f'#{t}')
    for row in arr:
        print(*row)
