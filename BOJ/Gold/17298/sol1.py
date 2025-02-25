# [G4] 오큰수

import sys
input = sys.stdin.readline

# STEP 1. 입력 받기
N = int(input())
A = list(map(int, input().split()))

# STEP 2. Stack 사용해서 오큰수 찾기
stack = [A[-1]]
NGE = [-1] * N

for i in range(N-2, -1, -1):
    while stack:
        if stack[-1] > A[i]:
            NGE[i] = stack[-1]
            break
        else:
            stack.pop()
    else:
        NGE[i] = -1
    stack.append(A[i])

# STEP 3. 출력 하기
for num in NGE:
    print(num, end=" ")