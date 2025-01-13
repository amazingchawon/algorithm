# [S1] 1946 신입 사원
# 시간 초과
import sys

# STEP 1. 입력 받기
T = int(sys.stdin.readline())

for t in range(T):
    answer = 0
    N = int(sys.stdin.readline())

    scores = []

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        scores.append((a, b))

    # STEP 2. 서류 순위 기준으로 정렬
    scores.sort()
    min_meeting_rank = float('inf')

    # STEP 3. 비교
    for _, meeting_rank in scores:
        if meeting_rank < min_meeting_rank:     # 자기보다 미팅 랭킹이 낮은 사람이 있다면 통과 가능
            answer += 1
            min_meeting_rank = meeting_rank     # 미팅 랭킹 갱신

    print(answer)