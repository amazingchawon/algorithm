# [S2] 6603 로또
# 직접 구현

chosen = []

def combinations(arr, idx, lv):
    # 6개 다 골랐으면,
    if lv == 6:
        for num in chosen:
            print(num, end=" ")
        print()
        return

    for i in range(idx, k):
        chosen.append(arr[i])
        combinations(arr, i+1, lv+1)
        chosen.pop()

while True:
    tc = list(map(int, input().split()))

    k, *S = tc          # k: 집합 S의 크기, S: 1-49 중 k개의 숫자가 담겨있는 집합

    if k == 0:
        break

    combinations(S, 0, 0)
    print()