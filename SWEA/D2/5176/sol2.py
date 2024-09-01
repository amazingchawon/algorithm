# [D2] 5176 이진탐색

def in_order(node):
    if node:
        in_order(left[node])
        tree.append(node)
        in_order(right[node])

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # STEP 1. 빈 완전 이진 트리 만들기
    tree = [0]
    # left, right tree의 왼쪽, 오른쪽 자식 인덱스 저장
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(1, N//2 + 1):
        left[i] = i * 2
        if i * 2 + 1 < N:
            right[i] = i * 2 + 1

    # STEP 2. 중위 순회하면서 숫자 넣기 -> tree 에 저장되는 것은 순회 순서
    in_order(1)

    print(f'#{t} {tree.index(1)} {tree.index(N//2)}')