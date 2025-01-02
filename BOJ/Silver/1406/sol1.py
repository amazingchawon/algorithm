# [S2] 1406 에디터
# 시간 초과

# STEP 1. 입력 받기
word = input()
M = int(input())

cursor = len(word)

# STEP 2. 명령어 수 만큼 반복
for m in range(M):
    action = input()
    if action.startswith('P'):          # 오른쪽에 새로운 문자 추가
        action, char = action.split()
        if cursor == len(word):
            word = word + char
        elif cursor == 0:
            word = char + word
        else:
            word = word[:cursor] + char + word[cursor:]
        cursor += 1
    elif action == 'L':                 # 왼쪽으로 커서 이동
        cursor = cursor - 1 if cursor > 0 else cursor
    elif action == 'D':                 # 오른쪽으로 커서 이동
        cursor = cursor + 1 if cursor < len(word) else cursor
    else:                               # 왼쪽 문자 하나 삭제
        if cursor != 0:
            word = word[:cursor-1] + word[cursor:]
            cursor -= 1

print(word)