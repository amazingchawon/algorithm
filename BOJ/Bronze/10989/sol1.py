# [B1] 10989 수 정렬하기 3
import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10001

for _ in range(N):
    numbers[int(input())] += 1

for i in range(1, len(numbers)):
    for j in range(numbers[i]):
        sys.stdout.write(f"{str(i)}\n")