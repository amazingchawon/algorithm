# [S5] 10814 나이순 정렬

N = int(input())

members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])

members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
