# [G4] 9935 문자열 폭발
import sys

# STEP 1. 입력 받기
word = list(sys.stdin.readline().strip())
bomb = sys.stdin.readline().strip()

length = len(bomb)      # 폭탄 글자의 길이
stack = []

for char in word:
    stack.append(char)  # 글자를 하나씩 추가

    if len(stack) >= length:                    # 폭탄 글자 길이보다 길다면 검사
        if ''.join(stack[-length:]) == bomb:    # 끝에 글자 paring 후 폭탄 글자와 비교
            for _ in range(length):
                stack.pop()

answer = ''.join(stack)
if answer == '':
    answer = 'FRULA'

print(answer)