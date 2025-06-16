# [G4] 2981 검문
# 실패

# STEP 1. 입력 받기
N = int(input())
arr = [int(input()) for _ in range(N)]

answer = []
min_num = min(arr)

# STEP 2. 2부터 min_num 순회 -> 나머지 같아지는 수 찾기
for num in range(2, min_num+1):
    tmp = set()                     # 나머지를 담을 짒합
    for i in range(N):              # arr 순회
        tmp.add(arr[i]%num)         # 나머지를 집합에 집어 넣기
    if len(tmp) == 1:               # 집합 길이 1개 == 모두 나머지 같음
        answer.append(num)          # 정답 배열에 추가

# STEP 3. 출력
print(*answer)