# [S2] 1874 스택 수열

# STEP 1. 입력 받기
N = int(input())
target = [int(input()) for _ in range(N)]
idx = 0

numbers = [i for i in range(1, N+1)]
stack = []
expr = []
is_possible = True

# STEP 2. 순회하며 수열 만들기
for num in target:
    while numbers and num >= numbers[0]:
        stack.append(numbers.pop(0))
        expr.append('+')
    if num == stack[-1]:
        stack.pop()
        expr.append('-')
    else:
        is_possible = False

if is_possible:
    for token in expr:
        print(token)
else:
    print('NO')