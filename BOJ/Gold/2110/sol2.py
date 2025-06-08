# [G4] 2110 공유기 설치
# 그리디, 시간 초과

# STEP 0. 설치 가능 여부 판단 함수 작성
def installable(dist):
    count = 1                           # 첫번째 집에는 공유기 반드시 설치
    last = homes[0]
    for i in range(1, N):
        if homes[i] - last >= dist:     # i번째 집과 직전 설치 집의 거리가 dist보다 크거나 같다면,
            count += 1                  # 공유기 설치
            last = homes[i]             # 마지막 설치 집 위치 갱신

    return count >= C

# STEP 1. 입력 받기
N, C = map(int, input().split())    # N : 집 개수, C : 공유기 개수
homes = sorted(list(int(input()) for _ in range(N)))    # homes : 집 오름차순으로 정렬한 배열

# STEP 2. 거리 늘려가며 최대 설치 거리 찾기
max_dist = homes[-1] - homes[0]
answer = 0

for diff in range(1, max_dist+1):
    if installable(diff):
        answer = diff

print(answer)
