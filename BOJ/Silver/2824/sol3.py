# [S1] 2824 최대 공약수

from math import gcd

# STEP 1. 입력 받기
N = int(input())
A_nums = list(map(int, input().split()))
M = int(input())
B_nums = list(map(int, input().split()))

# STEP 2. A, B 구하기
A = 1
B = 1

for a in A_nums:
    A *= a

for b in B_nums:
    B *= b

# STEP 3. 라이브러리 이용해서 최대공약수 구하기
answer = gcd(A, B)

# STEP 4. 출력: 10억 이상이면 앞에 0을 붙여 9자리 문자열 출력
if answer >= 10**9:
    print(str(answer)[-9:])
else:
    print(answer)  # 10억 미만이면 그대로 출력