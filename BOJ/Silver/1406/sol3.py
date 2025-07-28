# [S2] 1406 에디터
# 다시 풀이

# STEP 1. 입력 받기
left = list(input())    # left : 커서 왼쪽에 있는 문자들
right = []

M = int(input())        # 명령어 수

# STEP 2. 명령어 수행
for m in range(M):
    command = input()
    if command.startswith('P'):
        _, token = command.split()
        left.append(token)
    elif command == 'L' and left:
        right.append(left.pop())
    elif command == 'D' and right:
        left.append(right.pop())
    elif command == 'B' and left:
        left.pop()

# STEP 3. 출력
answer = ''.join(left + right[::-1])
print(answer)