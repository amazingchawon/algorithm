# [S4] 10828 스택

N = int(input())
stack = []

for _ in range(N):
    prompt = input().split()

    if prompt[0] == "push":
        stack.append(prompt[1])
    elif prompt[0] == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif prompt[0] == "size":
        print(len(stack))
    elif prompt[0] == "empty":
        print(0 if len(stack) else 1)
    else:
        print(stack[-1] if len(stack) else -1)