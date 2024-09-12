# [LV1] 17682 다트 게임

str_to_num = {'S': 1, 'D': 2, 'T': 3}

def solution(dartResult):
    idx = 0             # dartResult 순회하기 위한 idx 변수
    game = [0] * 3      # game 회차 별 결과를 담을 배열
    set_num = 0         # 게임 몇회차인지 체크할 idx 변수

    # STEP 1. 회차 나누기
    while set_num < 3:
        tmp = ['', 0, 1]
        # 점수|보너스|옵션 or 점수|보너스 중 무엇인지 판별
        while idx < len(dartResult):
            # 점수 부분
            if dartResult[idx].isdecimal():
                tmp[0] += dartResult[idx]
                idx += 1
            # 보너스 부분
            elif dartResult[idx] in {'S', 'D', 'T'}:
                tmp[1] = str_to_num.get(dartResult[idx])
                idx += 1
                # 옵션 부분 있나 없나 판별:
                if idx < len(dartResult) and dartResult[idx].isdecimal():
                    break
            # 옵션 부분
            else:
                if dartResult[idx] == '#':
                    tmp[2] = -1
                else:
                    tmp[2] = 2
                idx += 1
                break

        # STEP 2. 계산
        point, bonus, option = tmp
        point = int(point)
        # '#' 옵션이라면,
        if option == 2:
            if set_num > 0:
                game[set_num - 1] *= 2
            game[set_num] = (point**bonus)*option
        else:
            game[set_num] = (point**bonus)*option
        set_num += 1

    answer = sum(game)
    return answer