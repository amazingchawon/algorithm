# [D4] 1238 Contact

# import sys
# sys.stdin = open('input.txt', 'r')
from collections import deque

T = 10

for t in range(1, T+1):
    # L: 데이터 길이, S: 시작점, contact: {from, to, from, to, ...}
    L, S = map(int, input().split())
    contact = list(map(int, input().split()))
    N = max(contact)

    # STEP 1. 인접 리스트 만들기 (연락할 수 있는 사람 연결)
    # arr: 0번 사람 무시
    arr = [[] for _ in range(N+1)]

    for i in range(0, L, 2):
        p1, p2 = contact[i], contact[i+1]
        arr[p1].append(p2)

    # STEP 2. 연락 돌리기
    # BFS
    visited = [0] * (N+1)
    q = deque()
    q.append(S)
    visited[S] = 1

    while q:
        curr = q.popleft()
        for nxt in arr[curr]:
            if visited[nxt] == 0:
                q.append(nxt)
                visited[nxt] = visited[curr] + 1
    
    # STEP 3. 마지막으로 연락 받은 사람들 중 번호가 제일 큰 사람 찾기
    last = max(visited)         # 몇회차까지 돌았는지 기록
    for i in range(N, -1, -1):  # 거꾸로 순회 -> 번호 제일 큰 사람 찾기 위해
        if visited[i] == last:  # 마지막 회차에 전화받은 사람 찾으면
            answer = i          # 정답 기록
            break               # 반복 종료

    print(f'#{t} {answer}')