# [S2] 1927 최소 힙
# 최소 힙 구현
# 실패

# STEP 1. 힙 삽입 함수 정의
def enq(x):
    global last
    last += 1           # 마지막 노드 번호 갱신
    heap.append(x)      # 마지막 노드에 데이터 삽입
    c = last            # 자식 노드
    p = last//2         # 부모 노드
    while p >= 1 and heap[p] > heap[c]:         # 부모가 있는데 (p>=1) 부모가 더 크다면,
        heap[p], heap[c] = heap[c], heap[p]     # 자리 바꾸기
        c = p
        p //= 2

# STEP 2. 힙 삭제 함수 정의
def deq():
    global last
    tmp = heap[1]   # 루트의 키 값 보관
    heap[1] = heap[last]    # 마지막 숫자를 루트로 이동
    last -= 1               # 마지막 노드 번호 갱신
    p = 1
    c = p * 2
    while c <= last:        # 자식이 있다면,
        if c + 1 <= last and heap[c] > heap[c+1]:   # 오른쪽 자식이 있고, 더 작다면
            c += 1                                  # 오른쪽 자식하고 비교
        if heap[p] > heap[c]:                       # 부모가 더 크면,
            heap[p], heap[c] = heap[c], heap[p]     # 자리 바꾸기
            p = c
            c = p * 2
        else:
            break
    return tmp

N = int(input())
heap = [0]
last = 0

for _ in range(N):
    x = int(input())

    if x == 0:
        if last != 0:
            print(deq())
        else:
            print(0)
    else:
        enq(x)