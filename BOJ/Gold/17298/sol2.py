# [G4] 17298 오큰수

# STEP 1. 변수 할당
N = int(input())
numbers = list(map(int, input().split()))

NGE = []
stack = []

# STEP 2. 역순 순회 -> 오큰수 찾기
for i in range(N-1, -1, -1):
    num = numbers[i]

    while stack and stack[-1] <= num:
        stack.pop()

    if not stack:
        NGE.append(-1)
    else:
        NGE.append(stack[-1])

    stack.append(num)

# STEP 3. 출력
print(*NGE[::-1])