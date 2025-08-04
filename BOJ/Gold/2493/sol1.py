# [G5] 2493 탑
# 시간 초과

# STEP 1. 입력 받기
N = int(input())                        # N : 탑의 수
arr = list(map(int, input().split()))   # arr : 탑의 높이
result = [0 for _ in range(N)]          # 결과 담을 배열

# STEP 2. 뒤에서부터 순회
for i in range(len(arr)-1, -1, -1):
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]:
            result[i] = j + 1
            break

# STEP 3. 출력
print(*result)


