# [G3] 1939 중량제한
import heapq

# STEP 1. 입력 받기
N, M = map(int, input().split())    # N: 섬의 수, M: 다리 수

# STEP 1.1. 인접 리스트 만들기
adj = [[] for _ in range(N+1)]      # 인접 리스트

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

S, T = map(int, input().split())    # S: 시작 섬, T: 끝나는 섬

# STEP 2. Dijkstra 활용
pq = []
best = [0] * (N+1)                  # best : 시작 섬에서 i번째 섬까지 갔을 때 최대 중량
best[S] = 10**18

heapq.heappush(pq, (-best[S], S))

while pq:
    neg_w, curr = heapq.heappop(pq)
    w = -neg_w
    
    if best[curr] > w:              # 이미 갱신이 되어있다면,
        continue                    # 넘어가기

    if curr == T:                   # 도착 섬이라면,
        break                       # 종료 -> 최대 힙이기 때문에 이게 최선!

    for nxt, cost in adj[curr]:
        nxt_w = min(cost, w)

        if nxt_w > best[nxt]:       # 다음 섬으로 가는게 최대 중량이 낮아진다면,
            best[nxt] = nxt_w
            heapq.heappush(pq, (-nxt_w, nxt))

print(abs(best[T]))