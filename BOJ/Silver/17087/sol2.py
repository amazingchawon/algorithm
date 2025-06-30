# [S2] 17087 숨바꼭질 6

# STEP 1. 입력 받기
N, S = map(int, input().split())

# STEP 1-1. 동생들과 수빈이 사이 거리 차 구하기
siblings = list(map(lambda x: abs(int(x) - S), input().split()))

# STEP 2. 최대 공약수 함수 작성
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# STEP 3. siblings의 최대 공약수 구하기
while len(siblings) > 1:
    siblings.append((gcd(siblings.pop(), siblings.pop())))

print(siblings.pop())