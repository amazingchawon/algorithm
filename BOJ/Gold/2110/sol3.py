# [G4] 2110 공유기 설치
# 그리디, 이분 탐색

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

# STEP 2. 가운데 집에서 조정해가며 최대 설치 거리 찾기
answer = 0

start = 1
end = homes[-1] - homes[0]

while start <= end:
    mid = (start + end) // 2
    if installable(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
