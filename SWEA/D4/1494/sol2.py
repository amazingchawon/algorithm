# [D4] 1494 사랑의 카운슬러

import sys
sys.stdin = open('input.txt', 'r')

def make_couple(couple, matched):
    global answer

    if len(couple) == N:  # N마리 모두 커플이 되었다면,
        tmp = 0
        for w in range(0, N, 2):                    # 지렁이 커플 순회
            x1, y1 = worms[couple[w]]               # 지렁이 1의 좌표
            x2, y2 = worms[couple[w+1]]             # 지렁이 2의 좌표
            tmp += abs(x1-x2)**2 + abs(y1-y2)**2
            if answer < tmp:
                break
        if answer > tmp:    # answer보다 현재 커플 조합의 벡터 합이 작다면
            answer = tmp    # 갱신
        return

    # couple에는 지렁이 번호 기입
    for i in range(N):
        if not matched[i]:
            couple.append(i)
            matched[i] = 1
            make_couple(couple, matched)
            couple.pop()
            matched[i] = 0




T = int(input())

for t in range(1, T+1):
    N = int(input())        # N : 지렁이 수
    worms = [0] * N         # worms : 지렁이 좌표 저장 배열

    for i in range(N):
        worms[i] = list(map(int, input().split()))

    # STEP 1. N마리 모두 매칭되는 경우 찾기 (N//2쌍의 커플 매칭)
    answer = float('inf')
    used = [0] * N
    make_couple([], used)

    print(f'#{t} {answer}')
