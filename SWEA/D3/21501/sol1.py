# 21501 부분집합의 합

import sys
sys.stdin = open('input.txt', 'r')

def subset_arr():
    subsets = []
    tmp = [0] * 13

    for i in range(2):
        tmp[1] = i
        for j in range(2):
            tmp[2] = j
            for k in range(2):
                tmp[3] = k
                for l in range(2):
                    tmp[4] = l
                    for m in range(2):
                        tmp[5] = m
                        for n in range(2):
                            tmp[6] = n
                            for o in range(2):
                                tmp[7] = o
                                for p in range(2):
                                    tmp[8] = p
                                    for q in range(2):
                                        tmp[9] = q
                                        for r in range(2):
                                            tmp[10] = r
                                            for s in range(2):
                                                tmp[11] = s
                                                for t in range(2):
                                                    tmp[12] = t
                                                    subsets.append(tmp.copy())
    return subsets

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    subsets = subset_arr()
    answer = 0

    # subsets에서 부분집합 하나씩 순회
    for subset in subsets:
        subset_length = 0   # 부분집합 길이 기록 변수
        subset_sum = 0      # 부분집합 합 기록 변수

        # 부분집합의 길이, 합계산
        for i in range(len(subset)):
            if subset[i] == 1:      # 부분집합의 원소가 1이면
                subset_length +=1   # 부분집합 길이 증가
                subset_sum += i     # 부분집합 합 계산

        # N, K 조건에 맞는지 확인
        if subset_length == N and subset_sum == K:
            answer += 1

    print(f'#{t} {answer}')