# [G4] 1043 거짓말

# STEP 1. 입력 받기
N, M = map(int, input().split()) # N: 사람 수, M: 파티 수
true_set = set(list(map(int, input().split()))[1:])

parties = []

for _ in range(M):
    parties.append(set(list(map(int, input().split()))[1:]))

# STEP 2. 참을 말해야하는 사람 찾기
check = True

while check:                                # 더 이상 참을 말하는 사람을 추가할 필요 없을 때까지
    check = False
    index = []

    for i in range(len(parties)):           # 각 파티별에서
        party = parties[i]
        if true_set & party:                # 참을 말해야하는 사람이 포함해 있다면
            true_set = true_set | party     # 그 파티에 있는 전원에게 참을 말하기
            index.append(i)
            check = True

    for idx in reversed(index):
        parties.pop(idx)

# STEP 3. 거짓을 말해도 되는 파티 수 세기
answer = len(parties)

print(answer)