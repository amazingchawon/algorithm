# [D3] 5203 베이비진 게임

# import sys
# sys.stdin = open('input.txt', 'r')

def check(arr, index):
    arr = arr[:index+1]             # 아직 채워지지 않은 뒷 자리는 잘라버리기
    # run 체크
    for num in arr:
        if arr.count(num) >= 3:
            return True
        elif arr.count(num) == 2:
            arr.pop(arr.index(num))

    # triplet 체크
    arr.sort()
    for j in range(0, len(arr) - 2):
        if arr[j] + 2 == arr[j + 1] + 1 == arr[j + 2]:
            return True

    return False


def match(p1, p2):
    if p1:              # 플레이어 1이 조건을 달성했고,
        if not p2:      # 플레이어 2는 못했다면,
            return 1
        else:           # 플레이어 2도 달성을 했다면,
            return 0
    elif p2:            # 플레이어 1는 달성 못하고, 플레이어 2가 조건을 달성했다면,
        return 2
    return 0

T = int(input())

for t in range(1, T+1):
    cards = list(map(int, input().split()))
    player1 = [0] * 6       # player1 카드
    player2 = [0] * 6       # player2 카드
    player1_check = False
    player2_check = False

    for i in range(0, 12, 2):                               # 카드 한 장씩 받기
        player1[i//2] = cards[i]                            # 플레이어 1 받기
        if i >= 4:                                          # 3장 이상 받았으면
            player1_check = check(player1, i//2)            # run / triplet 체크
            answer = match(player1_check, player2_check)    # 플레이어 1, 2 대결
            if answer != 0:                                 # 무승부가 아니였으면,
                print(f'#{t} {answer}')                     # 출력
                break
        player2[i//2] = cards[i+1]                          # 플레이어 2 받기
        if i >= 4:                                          # 3장 이상 받았으면
            player2_check = check(player2, i//2)            # run / tripet 체크
            answer = match(player1_check, player2_check)    # 플레이어 1, 2 대결
            if answer != 0:                                 # 무승부가 아니었으면,
                print(f'#{t} {answer}')                     # 출력
                break
        if i == 10:
            print(f'#{t} 0')