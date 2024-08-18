# [D3] 4831 전기버스

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # K : 한 번 충전으로 갈 수 있는 정류장 수
    # N : 정류장 총 개수
    # M : 충전기 정류장 수
    K, N, M = map(int, input().split())

    stops = list(map(int, input().split()))     # 충전기 정류장 위치
    chargers = [1] + [0] * (N+1)                      # 충전기 위치 기록, 출발 위치에 충전기 있으니까 앞에 1 붙여주기

    for stop in stops:
        chargers[stop] = 1

    path = [0] * (N+1)                          # 지나온 정류장을 표시할 list
    position = 0                                # 버스 현재 위치
    answer = 0

    while position < N:                 # 마지막 정류장에 갈 때까지
        if chargers[position] == 1:     # 현재 위치가 충전소라면,
            answer += 1                 # 충전 횟수 증가
            path[position] += 1         # 방문 기록
            position += K               # 위치 변경, K만큼 이동
            continue
        elif chargers[position] == 0:   # 충전소가 아니라면
            position -= 1               # 한 칸 뒤로
        if path[position] == 1:         # 지나온 길이라면,
            answer = 0                  # 도착 불가
            break

    if answer == 0:
        print(f'#{t} {answer}')
    else:
        print(f'#{t} {answer-1}')   # 처음 충전소는 충전 횟수로 카운트 X