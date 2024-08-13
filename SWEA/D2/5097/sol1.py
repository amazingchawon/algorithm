# [D2] 5097 회전

import sys
sys.stdin = open('input.txt', 'r')

# 원형 큐 함수
def enqueue(arr, item):
    global rear
    rear = (rear + 1) % len(arr)
    arr[rear] = item

def dequeue(arr):
    global front
    front = (front + 1) % len(arr)
    return arr[front]

T = int(input())    # 테스트 케이스 수

for t in range(1, T+1):
    N, M = map(int, input().split())        # N : 숫자 수, M : 반복 횟수
    arr = list(map(int, input().split()))
    arr = [0] + arr                         # 원형큐 구현하기 위해 앞에 원소 하나 추가

    front = 0   # 가장 먼저 삽입된 원소 인덱스 위치를 나타내는 변수
    rear = N    # 가장 최근에 삽입된 원소 인덱스 위치를 나타내는 변수

    # M번 반복
    for _ in range(M):
        enqueue(arr, dequeue(arr))  # 제일 오래된 원소 빼와서, 제일 뒤에 붙여주기

    print(f'#{t} {arr[(front+1) % len(arr)]}')  # 현재 front 원소가 가장 앞에 있는 것, 원형 큐라 나머지 연산자 사용해서 인덱싱