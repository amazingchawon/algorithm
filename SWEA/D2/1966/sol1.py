# [D2] 1966 숫자를 정렬하자

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    answer = bubble_sort(arr)
    print(f'#{t}', end=' ')
    print(*answer)
    print()