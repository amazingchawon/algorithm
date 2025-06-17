# [S3] 2407 조합

# STEP 1. 입력 받기
n, m = map(int, input().split())

# STEP 2. 분모, 분자에 들어갈 값 구하기
top = 1
bottom = 1

# STEP 2-1. nCm == nCn-m을 이용해서, 계산 횟수 줄이기
if m > n - m:
    m = n - m

# STEP 2-2. 1씩 줄여가며 분모, 분자 계산
for i in range(m):
    top *= n - i
    bottom *= m - i

print(top//bottom)