# [G5] 2447 별 찍기 - 10
def make_star(x, y, size):
    if size == 1:
        star[x][y] = '*'
        return

    next_size = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            make_star(x + (i * next_size), y + (j * next_size), next_size)

N = int(input())
star = [[' ' for _ in range(N)] for _ in range(N)]
make_star(0, 0, N)

for row in star:
    print(''.join(row))