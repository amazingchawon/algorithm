# [S2] 1182 부분수열의 합

# STEP 1. 입력 받기
N, S = map(int, input().split())        # N : arr의 길이, S : 요구하는 부분 수열의 합
arr = list(map(int, input().split()))

answer = 0

# STEP 2. DFS로 탐색
def dfs(idx, total):
    global answer

    # 마지막 원소까지 봤을떄,
    if idx == N:
        if total == S:
            answer += 1
        return

    # 현재 원소 포함
    dfs(idx + 1, total + arr[idx])
    # 현재 원소 미포함
    dfs(idx + 1, total)

dfs(0, 0)

# 공집합 제외, S == 0이면 하나 빼주기
if S == 0:
    answer -= 1

print(answer)