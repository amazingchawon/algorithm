while True:
    game = input().strip()

    if game == 'end':
        break

    # 'X'와 'O' 개수 체크
    cnt_X = game.count('X')
    cnt_O = game.count('O')

    # 전제 X는 O보다 1개 많거나, 같은 개수여야 함
    if not (cnt_X == cnt_O or cnt_X == cnt_O + 1):
        print("invalid")
        continue

    # 승리 조건 확인
    def check_winner(player):
        return (
            any(game[i] == game[i + 3] == game[i + 6] == player for i in range(3)) or  # 세로
            any(game[i] == game[i + 1] == game[i + 2] == player for i in range(0, 9, 3)) or  # 가로
            (game[0] == game[4] == game[8] == player) or  # 대각선 1
            (game[2] == game[4] == game[6] == player)  # 대각선 2
        )

    X_wins = check_winner('X')
    O_wins = check_winner('O')

    # 예외 1. 승자 두명 불가
    if X_wins and O_wins:
        print("invalid")
        continue

    # 예외 2. X가 이기면 X 수가 한 개 더 많아야 함
    if X_wins and cnt_X != cnt_O + 1:
        print("invalid")
        continue

    # 예외 3. O가 이기면 O 수가 한 개 더 많아야 함
    if O_wins and cnt_X != cnt_O:
        print("invalid")
        continue

    # 예외 4. 승자가 없다면 빈칸이 없어야 함
    if not X_wins and not O_wins and game.count('.') > 0:
        print("invalid")
        continue

    print("valid")
