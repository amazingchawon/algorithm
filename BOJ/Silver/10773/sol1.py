# [S4] 10773 제로

# STEP 1. K 입력 받기
K = int(input())        # K는 총 반복 횟수
stack = []

for _ in range(K):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))