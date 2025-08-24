# [G5] 1914 하노이 탑

N = int(input())
print(2**N - 1)

if N <= 20:
    def move(num, start, end, temp):
        if num == 1:
            print(start, end)
        else:
            move(num-1, start, temp, end)
            print(start, end)
            move(num-1, temp, end, start)

    move(N, 1, 3, 2)