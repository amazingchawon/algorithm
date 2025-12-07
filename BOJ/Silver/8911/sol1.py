# [S3] 8911 거북이

# STEP 1. 변수 설정
T = int(input())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 방향들

for _ in range(T):
    command = input()
    x_paths = [0]        # 지나간 곳의 x좌표를 저장할 배열
    y_paths = [0]        # 지나간 곳의 y좌표를 저장할 배열
    curr_x = 0
    curr_y = 0

    # STEP 2. 명령 수행
    idx = 0             # d의 인덱스

    for c in command:
        if c == 'F':
            dx, dy = d[idx]
            curr_x += dx
            curr_y += dy
            x_paths.append(curr_x)
            y_paths.append(curr_y)
        elif c == 'B':
            dx, dy = d[(idx + 2) % 4]   # 반대 방향으로 이동
            curr_x += dx
            curr_y += dy
            x_paths.append(curr_x)
            y_paths.append(curr_y)
        elif c == 'L':
            idx = (idx - 1) % 4
        else:
            idx = (idx + 1) % 4

    # STEP 3. 직사각형 넓이 계산
    answer = (max(x_paths) - min(x_paths)) * (max(y_paths) - min(y_paths))

    print(answer)