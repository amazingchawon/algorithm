# [S3] 후위 표기식2

# STEP 1. 입력받기
N = int(input())
expr = input()
numbers = [int(input()) for _ in range(N)]

# STEP 2. 게산하기
stack = []

for token in expr:
    if 'A' <= token <= 'Z':
        stack.append(numbers[ord(token) - 65])
    else:
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            stack.append(a / b)

# STEP 3. 출력
print(f"{stack[-1]:.2f}")