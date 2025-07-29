# [S2] 10799 쇠막대기

# STEP 1. 입력받기 / 변수 생성
seq = input()
cnt = 0         # 몇개의 조각으로 나뉘는지 저장할 변수
stack = []      # 괄호를 저장할 stack

# STEP 2. 입력값 순회 -> 자르기
idx = 0
while idx < len(seq):
    if seq[idx] == '(':
        if idx+1 < len(seq) and seq[idx+1] == ')':  # ()가 연달아 들어올 때(== 레이저 일때)
            cnt += len(stack)
            idx += 1
        else:
            stack.append('(')
    else:
        stack.pop()
        cnt += 1
    idx += 1

# STEP 3. 답 출력
print(cnt)