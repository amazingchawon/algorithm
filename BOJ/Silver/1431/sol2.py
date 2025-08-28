# [S3] 1431 시리얼 번호

# 숫자 합 계산 함수
def calc_sum(num):
    sum = 0
    for char in num:
        if char.isdigit():
            sum += int(char)

    return sum

N = int(input())

serial_nums = [input() for _ in range(N)]

serial_nums.sort(key = lambda x : (len(x), calc_sum(x), x))

for num in serial_nums:
    print(num)