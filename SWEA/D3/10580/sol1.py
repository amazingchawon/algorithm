# [D3] 10580 전봇대

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    answer = 0

    for i in range(N):
        A, B = map(int, input().split())
        arr.append([A, B])
    
    for i in range(N):
        line = arr[i]
        for j in range(i+1, N):
            other_line = arr[j]
            if (line[0] > other_line[0] and line[1] < other_line[1]) or (line[0] < other_line[0] and line[1] > other_line[1]) :
                answer += 1
    
    print(f'#{t} {answer}')