# [D3] 1244 최대 상금

import sys
sys.stdin  = open('input.txt', 'r')

def combination(combi, start):
    if len(combi) == 2:
        combinations.append(combi[:])
    for j in range(start, len(num)):
        if len(combi) == 0 or combi[-1] != j:     # 직전에 같은 숫자만 나오지 않았더라면, j는 여러번 나와도 됨
            combi.append(j)
            combination(combi, j)
            combi.pop()

def permutation(perm):
    global answer
    if len(perm) == time:
        tmp = num[:]
        for x, y in perm:
            tmp[x], tmp[y] = tmp[y], tmp[x]
        number = int(''.join(tmp))
        if answer < number:
            answer = number
        return
    for j in range(len(combinations)):
        perm.append(combinations[j])
        permutation(perm)
        perm.pop()

T = int(input())

for t in range(1, T+1):
    num, time = input().split()     # num : 숫자판 정보, time : 교환 횟수
    answer = int(num)
    num = list(num)
    time = int(time)
    combinations = []                      # 순열 저장할 배열

    combination([], 0)
    permutation([])


    print(f'#{t} {answer}')