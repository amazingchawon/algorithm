# [G5] 14719 빗물

# STEP 1. 변수 정의
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

answer = 0

# STEP 2. 투 포인터 알고리즘 적용
left, right = 0, W-1
left_max, right_max = blocks[left], blocks[right]

while left < right:
    if left_max <= right_max:
        left += 1
        left_max = max(left_max, blocks[left])
        answer += max(0, left_max - blocks[left])
    else:
        right -= 1
        right_max = max(right_max, blocks[right])
        answer += max(0, right_max - blocks[right])

print(answer)