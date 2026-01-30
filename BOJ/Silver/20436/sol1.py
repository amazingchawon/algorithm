# [S4] 20436 ZOAC 3

# STEP 1. 입력 받기
# STEP 1.1. 키보드 구성
tmp_1 = 'qwertyuiop'
tmp_2 = 'asdfghjkl'
tmp_3 = 'zxcvbnm'

keyboard = dict()

for y in range(len(tmp_1)):
    if y < 5:
        keyboard[tmp_1[y]] = (1, y, 0)  # x좌표, y좌표, 왼손
    else:
        keyboard[tmp_1[y]] = (1, y, 1)  # x좌표, y좌표, 오른손

for y in range(len(tmp_2)):
    if y < 5:
        keyboard[tmp_2[y]] = (2, y, 0)
    else:
        keyboard[tmp_2[y]] = (2, y, 1)

for y in range(len(tmp_3)):
    if y < 4:
        keyboard[tmp_3[y]] = (3, y, 0)
    else:
        keyboard[tmp_3[y]] = (3, y, 1)

pos_l, pos_r = input().split()
position = [keyboard.get(pos_l), keyboard.get(pos_r)]

target = input().strip()
answer = 0

# STEP 2. 문자열 완성 시간 구하기
for t in target:
    tx, ty, hand = keyboard.get(t)
    lx, ly, lhand = position[0]
    rx, ry, rhand = position[1]

    if hand == 0:
        answer += (abs(lx - tx) + abs(ly - ty))
        position[0] = (tx, ty, 0)
    else:
        answer += (abs(rx - tx) + abs(ry - ty))
        position[1] = (tx, ty, 0)
    answer += 1

print(answer)
