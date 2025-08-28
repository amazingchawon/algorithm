# [B1] 2947 나무 조각

def switch(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)

woods = list(map(int, input().split()))
sorted_woods = sorted(woods)

while woods != sorted_woods:
    switch(woods)
