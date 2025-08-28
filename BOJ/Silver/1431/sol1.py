# [S3] 1431 시리얼 번호

# 숫자 합 계산 함수
def calc_sum(num):
    sum = 0
    for char in num:
        if ord(char) <= 57:
            sum += ord(char) - 48

    return sum

# 사전순 비교 함수
def check_ord(num1, num2):
    for i in range(len(num1)):
        if ord(num1[i]) < ord(num2[i]):
            return [num1, num2]
        elif ord(num1[i]) > ord(num2[i]):
            return [num2, num1]
        else:
            continue

N = int(input())

serial_nums = [input() for _ in range(N)]

# STEP 1. 길이순 정렬
serial_nums.sort(key = lambda x : len(x))

for i in range(N-1):
    for j in range(i+1, N):
        num1, num2 = serial_nums[i], serial_nums[j]
        if len(num1) == len(num2):
            # STEP 2. 숫자 합 정렬
            if calc_sum(num1) > calc_sum(num2):
                serial_nums[i], serial_nums[j] = num2, num1 # 교환
            elif calc_sum(num1) < calc_sum(num2):
                continue
            # STEP 3. 알파벳 숫 정렬
            else:
                serial_nums[i], serial_nums[j] = check_ord(num1, num2)

for num in serial_nums:
    print(num)