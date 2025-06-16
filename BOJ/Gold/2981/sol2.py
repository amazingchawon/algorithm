# [G4] 2981 검문

from math import gcd

# STEP 1. 입력 받기
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()  # 정렬해주기

answer = []

# STEP 2. 인접한 수들의 차이로 GCD 구하기
diffs = [arr[i] - arr[i-1] for i in range(1, N)]

gcd_value = diffs[0]                    # 처음값 빼두고
for diff in diffs[1:]:
    gcd_value = gcd(gcd_value, diff)    # 계속 gcd 구하기

# STEP 3. gcd_value의 약수 찾기
for num in range(2, int(gcd_value**0.5) + 1):
    if gcd_value % num == 0:
        answer.append(num)
        if num != gcd_value // num:         # num가 gcd_value//num과 다르면
            answer.append(gcd_value//num)   # gcd_value//num도 추가

answer.append(gcd_value)
answer.sort()

# STEP 4. 출력
print(*answer)