# [G5] 2447 별 찍기 - 10
def make_star(size):
    if size == 3:
        return ['***', '* *', '***']

    next_size = size//3
    arr = make_star(next_size)
    row1 = [row * 3 for row in arr]
    row2 = [row + ' ' * next_size + row for row in arr]
    row3 = row1
    return row1 + row2 + row3

N = int(input())
star = make_star(N)

for line in star:
    print(line)