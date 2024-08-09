# [D2] 4880 토너먼트 카드게임

import sys
sys.stdin = open('input.txt', 'r')

def rsp(team1, team2):
    if len(team1) == 1 and len(team2) == 1: # 팀에 한명씩 남았을 경우
        player1 = players[team1[0]] # team1에 1명 있는 팀원이 낸 카드
        player2 = players[team2[0]] # team2에 1명 있는 팀원이 낸 가드
        if player1 == '1' :         # 가위를 냈을 경우,
            if player2 == '2':      # 졌을 경우,
                return team2
            else:                   # 이겼을 경우 or 비겼을 경우,
                return team1
        if player1 == '2' :         # 바위를 냈을 경우,
            if player2 == '3':      # 졌을 경우,
                return team2
            else:
                return team1        # 이겼을 경우 or 비겼을 경우,
        if player1 == '3' :         # 보를 냈을 경우,
            if player2 == '1':      # 졌을 경우,
                return team2
            else:
                return team1        # 이겼을 경우 or 비겼을 경우,
    if len(team1) == 2 and len(team2) == 1: # 부전승이 생기는 경우
        return rsp(rsp([team1[0]], [team1[1]]), team2)
    else:
        team1_1 = team1[0:(len(team1)+1)//2]    # [1, 2, 3] 일 경우 [1, 2]와 [3]으로 팀을 나눠야함 -> (len(team1)+1) 을 해주고 2로 나눠줘야함
        team1_2 = team1[(len(team1)+1)//2:]
        team2_1 = team2[0:(len(team2)+1)//2]
        team2_2 = team2[(1+len(team2))//2:]
        return rsp(rsp(team1_1, team1_2), rsp(team2_1, team2_2))

T = int(input())

for t in range(1, T+1):
    # 입력 받기
    N = int(input())        # 참가한 플레이서 수
    players = {}            # 참가자 번호와 카드를 기록할 dict
    cards = input().split() # 참가자 카드 입력받기

    # players dict 완성
    for i in range(1, N+1):
        players[i] = cards[i-1] # 참가자 번호는 1번부터 시작, cards 인덱스 1개 뺴줘야함

    # 가위바위보 게임
    team = list(players.keys())
    team1 = team[0:(len(team)+1)//2]
    team2 = team[(len(team)+1)//2 :]
    answer = rsp(team1, team2)
    print(f'#{t} {answer[0]}')