# [S2] 10799 쇠막대기

# STEP 1. 입력받기 / 변수 생성
seq = input()
cnt = 0         # 몇개의 조각으로 나뉘는지 저장할 변수
stack = []      # 괄호를 저장할 stack

# STEP 2. 입력값 순회 -> 자르기
for i in range(len(seq)):
    if seq[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if seq[i-1] == '(': # ()가 연달아 나왔을 경우 (== 레이저일경우)
            cnt += len(stack)
        else:
            cnt += 1

# STEP 3. 답 출력
print(cnt)