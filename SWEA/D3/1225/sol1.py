# [D3] 1225 암호생성기

import sys
sys.stdin = open('input.txt', 'r')

# 원형큐 함수
def dequeue(arr):
    global front
    front = (front + 1) % len(arr)
    return arr[front]

def enqueue(arr, item):
    global rear
    rear = (rear + 1) % len(arr)
    arr[rear] = item

for _ in range(10):
    N = int(input())    # 문제 번호
    data = list(map(int, input().split()))  # 암호 배열
    data = [0] + data                       # front 값을 갱신해서 rear 다음 인덱스에 넣어주기 위해 data 앞에 0 추가

    front = 0   # 현재 front 값
    rear = 8    # 현재 rear 값, 배열의 마지막이 가장 최근에 추가 된 것
    cnt = 1     # 1번 반복할 때마다 증가시킬 변수

    while True:
        tmp = dequeue(data)             # 제일 오래전에 들어온 값을 tmp에 저장

        if tmp - cnt <= 0:              # 비밀번호 갱신 종료 조건 : 변환한 값이 0보다 작아지면
            enqueue(data, 0)            # 0으로 추가
            break                       # 반복 종료
        else:
            enqueue(data, tmp - cnt)    # tmp에 cnt만큼 뺀 것 queue에 추가

        if cnt == 5:                    # cnt가 현재 5라면
            cnt = 1                     # 다시 1로 내려주기
        else:                           # 아니라면
            cnt += 1                    # 1 추가

    # 답 출력
    print(f'#{N}', end=' ')             # 번호 출력
    for i in range(front, front+8):     # front부터 출력
        index = (i+1) % 9               # index 변환, data의 전체 길이인 9로 나누어 줌
        print(data[index], end=' ')     # 한 줄에 출력하기 위해 end 조건
    print()