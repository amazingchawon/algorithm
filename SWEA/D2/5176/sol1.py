# [D2] 5176 이진탐색

# def insert(T, num):
#     T.append(num)
#     child = T.index(num)
#     while child:
#         parent = child // 2
#         if T[parent] < T[child]:
#             T[parent], T[child] = T[child], T[parent]
#             child = parent

def insert(G, node, num):
    p = G[node]
    c_l_i = node*2
    c_r_i = node*2 + 1
    c_l = G[c_l_i]
    c_r = G[c_r_i]


    if G[node] > num:   # 왼쪽 트리로
        if G[node*2] == 0:  # 왼쪽 자식 비어있다면,
            G[node*2] = num
        else:
            insert(G, node*2, num)
    else:
        if G[node*2+1] == 0:  # 왼쪽 자식 비어있다면,
            G[node*2+1] = num
        else:
            insert(G, node*2+1, num)
T = int(input())

for t in range(1, T+1):
    N = int(input())

    # STEP 1. root 노드에 들어갈 숫자 찾기
    # 1 2 3 4 5 6 -> 4가 들어가야함
    # 1 2 3 4 5 6 7 -> 4가 들어가야함
    root = N//2 + 1

    tree = [0, root] + [0]*(N-1)
    # 나머지 넣어주기
    for i in range(1, N+1):
        if i != root:           # root가 아닐때만 넣어주기
            insert(tree, 1, i)

    print(f'#{t} {tree[0]} {tree[N//2]}')