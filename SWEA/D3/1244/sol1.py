# [D3] 1244 최대 상금

import sys
sys.stdin  = open('input.txt', 'r')

def permutation(perm, start):
    global answer, cnt
    if len(perm) == 2*time:
        tmp = num[:]
        for i in range(0, len(perm), 2):
            tmp[perm[i]], tmp[perm[i+1]] = tmp[perm[i+1]], tmp[perm[i]]
        number = int(''.join(tmp))
        if answer < number:
            answer = number
        return
    for j in range(start, len(num)):
        if len(perm) == 0 or perm[-1] != j:     # 직전에 같은 숫자만 나오지 않았더라면, j는 여러번 나와도 됨
            perm.append(j)
            if len(perm) % 2 == 0:
                permutation(perm, 0)
            else:
                permutation(perm, j)
            perm.pop()

T = int(input())

for t in range(1, T+1):
    num, time = input().split()     # num : 숫자판 정보, time : 교환 횟수
    answer = int(num)
    num = list(num)
    time = int(time)

    permutation([], 0)

    print(f'#{t} {answer}')