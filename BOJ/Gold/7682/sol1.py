백준 문제 7682야

# [G5] 7682 틱택토

while True:
    game = input()

    # 종료 조건
    if game == 'end':
        break

    is_vaild = True

    # 조건 2. 가로 3개 or 세로 3개 동일
    for i in range(3):
        if game[i] == game[i+3] == game[i+6]:
            break
        elif game[i*3] == game[(i*3) + 1] == game[(i*3) + 2]:
            break
        else:
            is_vaild = False

    # 조건 3. 대각선 동일
    if game[0] == game[4] == game[8] or game[2] == game[4] == game[6]:
        is_vaild = True

    # 조건 1. O 개수가 X 보다 많을 수 없다. (같거나 X가 하나 많아야함)
    if not (game.count('O') == game.count('X') or game.count('O') + 1 == game.count('X')):
        is_vaild = False

    if is_vaild:
        print('vaild')
    else:
        print('invaild')