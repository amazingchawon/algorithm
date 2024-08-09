# [D4] 1219 길찾기

import sys
sys.stdin = open('input.txt', 'r')

# start 노드에서 end 노드로 갈 수 있는지 알려주는 함수
def search(start, end, V):
    stack = [start]     # 노드를 탐색하면서 사용할 스택
    visited = [0] * (V+1)
    
    while stack:    # 스택에 숫자가 남아있는 동안
        # if end in stack:          # end 노드에 도달했다면
        #     find = 1
        #     break

        current = stack.pop()       # 현재 조사할 노드

        if current == end:          # end 노드에 도달했다면
            find = 1
            break

        if visited[current] == 0:       # 방문하지 않은 노드라면
            visited[current] = 1        # 방문 표기
            for next in range(V, -1, -1):     # 현재 노드에서 갈 수 있는 다음 노드 찾기
                if adj_matrix[current][next] == 1 and visited[next] == 0:  # 현재 노드에서 연결되어있는 노드 찾기
                    stack.append(next)
    else:   # break에 걸리지 않았다면
        find = 0
    
    return find
    

for t in range(10):
    # T : 테스트케이스 번호
    # N : 간선 수
    T, N = map(int, input().split())

    data = list(map(int, input().split())) # 노선 정보 저장한 리스트

    # 인접행렬 만들기
    adj_matrix = [[0]*100 for _ in range(100)]

    for i in range(N):
        v1 = data[i*2]
        v2 = data[i*2 + 1]
        adj_matrix[v1][v2] = 1

    print(f'#{T} {search(0, 99, 99)}')
    # for arr in adj_matrix:
    #     print(arr)