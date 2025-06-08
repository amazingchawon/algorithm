# [S3] 1929 소수 구하기

M, N = map(int, input().split())

# STEP 1. 에라토스테네스의 체
numbers = [ num for num in range(0, N+1)]   # numbers : 0부터 N까지 1로 채운 배열
numbers[1] = 0                          # 기초 수인 1을 제외

for i in range(2, N+1):
    if numbers[i]:                      # i가 아직 안 지워졌으면,
        for j in range(i+i, N+1, i):    # j의 배수들을
            numbers[j] = 0              # 지우기

# STEP 2. 체에 남아있는 숫자 중 M 이상만 출력
for num in numbers:
    if num != 0 and num >= M:
        print(num)