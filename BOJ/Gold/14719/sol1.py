# [G5] 14719 빗물

# STEP 1. 변수 구성
H, W = map(int, input().split())            # H, W: 2차원 세계의 세로, 가로 길이
grid = [[0] * W for _ in range(H)]          # 2차원 세계

heights = list(map(int, input().split()))   # 빌딩의 높이

answer = 0

# STEP 1.1 빌딩 그리기
for idx in range(W):
    for i in range(heights[idx]):
        grid[H-1-i][idx] = 1

# STEP 2. 빗물 채우기
for x in range(H):
    for y in range(W):
        if grid[x][y] == 1:                 # 건물이라면,
            ty = y + 1
            tmp = 0
            while ty < W: # 그 줄 순회
                if grid[x][ty] == 0:        # 빗물이 고일 수 있는 곳이라면,
                    tmp += 1                # 일단 저장
                elif grid[x][ty] == 1:      # 벽을 만나면
                    answer += tmp           # 빗물 고이기 가능
                    break
                ty += 1                     # 다음칸 체크

print(answer)