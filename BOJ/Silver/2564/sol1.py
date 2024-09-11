# [S1] 2564 경비원

# import sys
# sys.stdin = open('input.txt', 'r')

N, S, W, E = (1, 2, 3, 4)

# STEP 1. input 받기
w, h = map(int, input().split())    # w: 블록 가로, h : 블록 세로
X = int(input())                    # X : 상점 수

# 가게 위치 저장 + 동근이 위치까지 저장
stores = []
for _ in range(X+1):
    # d: 동서남북 방향, p: 왼쪽/위쪽으로부터 거리
    d, p = map(int, input().split())

    # 북이나 남쪽에 위치하면 -> (방향, 왼쪽, 오른쪽) 튜플로 저장
    if d == N or d == S:
        stores.append((d, p, w-p))
    # 동이나 서쪽에 위치하면 -> (방향, 위쪽, 아래쪽) 튜플로 저장
    else:
        stores.append((d, p, h-p))

# 동근이 (방향, 왼/위, 오/아래)
x, y1, y2 = stores.pop()

# STEP 2. 상점 순회 -> 동근이 - 각 상점 별 최단 거리 구하기
answer = 0

for store in stores:
    d, p1, p2 = store

    position = {d, x}

    if len(position) == 1:          # 가게랑 동근이랑 같은 쪽에 있을 때
        answer += abs(p1-y1)
    elif position == {N, S}:        # 가게, 동근 - 북, 남 위치할 때
        tmp1 = p1 + y1 + h          # 시계방향 합
        tmp2 = p2 + y2 + h          # 반시계방향 합
        answer += min(tmp1, tmp2)   # 둘 중 작은 값 answer에 추가
    elif position == {W, E}:        # 가게, 동근 - 동, 서 위치할 때
        tmp1 = p1 + y1 + w
        tmp2 = p2 + y2 + w
        answer += min(tmp1, tmp2)
    elif position == {N, W}:        # 가게, 동근 - 북, 서 위치할 때
        answer += p1 + y1           # 이 경우 시계방향이 무조건 짧을 수 밖에 없음
    elif position == {N, E}:
        if d == N:
            answer += p2 + y1
        else:
            answer += p1 + y2
    elif position == {S, E}:
        answer += p2 + y2
    elif position == {S, W}:
        if d == S:
            answer += p1 + y2
        else:
            answer += p2 + y1

print(answer)