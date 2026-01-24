# [G1] 2933 미네랄
def find_cluster(cave):
    visited = [[0] * C for _ in range(R)]
    clusters = []

    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x' and not visited[r][c]:
                cluster = {(r, c)}
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()
                    visited[x][y] = 1

                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        tx, ty = x + dx, y + dy
                        if 0 <= tx < R and 0 <= ty < C and not visited[tx][ty] and cave[tx][ty] == 'x':
                            stack.append((tx, ty))
                            cluster.add((tx, ty))

                clusters.append(cluster)

    return clusters

def drop_cluster(cluster, cave):
    d = R

    # STEP 1. 떨어지는 거리 계산
    for x, y in cluster:
        # STEP 1.1. 바닥에 붙어있을 경우
        if x == R-1:
            return cave

        # STEP 1.2. 어디까지 내려갈 수 있는지 체크
        dist = 0
        nx = x + 1
        while nx < R:
            # 아래 칸이 클러스터 내부면 내려가도 됨
            if (nx, y) in cluster:
                nx += 1
                continue

            # 아래 칸이 다른 미네랄이면 멈춤
            if cave[nx][y] == 'x':
                break

            # 아래 칸이 빈칸이면 더 내려갈 수 있음
            dist += 1
            nx += 1

        d = min(d, dist)

    # STEP 2. 떨어트리기
    if d == 0:
        return cave

    for x, y in cluster:
        cave[x][y] = '.'

    for x, y in cluster:
        cave[x + d][y] = 'x'

    return cave

# STEP 1. 입력 받기
R, C = map(int, input().split())

# STEP 1.1. 동굴 입력
cave = [[0] * C for _ in range(R)]

for r in range(R):
    tmp = input()
    for c in range(C):
        cave[r][c] = tmp[c]

N = int(input())
heights = list(map(int, input().split()))

# STEP 2. 막대 던지기
left = True

for h in heights:
    h = abs(h - R)
    # STEP 2.1. 왼쪽에서 던질때
    if left:
        for c in range(C):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                break

    # STEP 2.2. 오른쪽에서 던질때
    else:
        for c in range(C-1, -1, -1):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                break

    # STEP 2.3 클러스터 찾기
    clusters = find_cluster(cave)

    # STEP 2.4 떨어트리기
    for cluster in clusters:
        cave = drop_cluster(cluster, cave)

    left = False if left else True

for row in cave:
    print("".join(row))
