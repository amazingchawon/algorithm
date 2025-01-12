# [S1] 1946 신입 사원
# 시간 초과
import sys

# STEP 1. 입력 받기
T = int(sys.stdin.readline())

for t in range(T):
    answer = 0
    N = int(sys.stdin.readline())

    scores = [0] * N

    for n in range(N):
        score = list(map(int, sys.stdin.readline().split())) + [n]
        scores[n] = score

    # STEP 2. 정렬
    paper = sorted(scores, key=lambda x: x[0])        # 첫번째 인덱스 기준으로 정렬
    meeting = sorted(scores, key=lambda x: x[1])      # 두번째 인덱스 기준으로 정렬

    for n in range(N):
        paper[n] = paper[n][2]
        meeting[n] = meeting[n][2]

    # STEP 3. 비교
    for i in range(N):
        paper_ranking = paper.index(i)
        meeting_ranking = meeting.index(i)

        # i번째 사원과 비교했을 때, 면접, 서류 점수 둘 중 하나라도 높은 지원자들을 담은 배열 만들기
        # i번째 사원보다 서류 순위 높은 사람들 / 면접 순위 높은 사람들 구하기
        # 그 두 그룹의 교집합 구하기 -> 교집합이 있을 경우, 탈락하는 조건
        tmp = set(paper[:paper_ranking]).intersection(set(meeting[:meeting_ranking]))
        if len(tmp) == 0:
            answer += 1

    print(answer)