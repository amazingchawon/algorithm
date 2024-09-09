# [D3] 21501 부분집합의 합

# STEP 1. 1-12 모든 부분집합 만들기
A = [i for i in range(1, 13)]

subsets = []

for i in range(1<<12):
    tmp = set()
    for idx in range(12):
        if i & (1<<idx):
            tmp.add(A[idx])
    subsets.append(tmp)

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    answer = 0

    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            answer += 1

    print(f'#{t} {answer}')