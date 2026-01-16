# [G5] 14719 빗물

# STEP 1. 변수 정의
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0

# STEP 2. 높이 순회
for w in range(1, W-1):
    left = max(blocks[:w])          # 왼쪽에서 제일 높은 것
    right = max(blocks[w+1: ])      # 오른쪽에서 제일 높은 것
    m = min(left, right)            # 둘 중 더 낮은 것 -> 빗물이 고일 수 있는 최대 높이
    if m > blocks[w]:
        answer += m - blocks[w]

print(answer)