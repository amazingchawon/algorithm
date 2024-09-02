# [D2] 5176 이진탐색

def in_order(node):
    global num
    if node <= N:
        in_order(node*2)
        tree[node] = num
        num += 1
        in_order(node*2 + 1)

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # STEP 1. 빈 완전 이진 트리 만들기
    tree = [0] * (N+1)


    # STEP 2. 중위 순회하면서 숫자 넣기
    num = 1
    in_order(1)

    print(f'#{t} {tree[1]} {tree[N//2]}')