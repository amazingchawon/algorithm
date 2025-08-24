# [S2] 2630 색종이 만들기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white_cnt = 0
blue_cnt = 0

def color_check(x, y, d):
    global white_cnt, blue_cnt

    color = arr[x][y]
    is_same = True

    for tx in range(x, x+d):
        for ty in range(y, y+d):
            if color != arr[tx][ty]:
                is_same = False

            if not is_same:
                nd = d//2
                color_check(x, y, nd)
                color_check(x + nd, y, nd)
                color_check(x, y + nd, nd)
                color_check(x + nd, y + nd, nd)
                return

    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


color_check(0, 0, N)
print(white_cnt)
print(blue_cnt)