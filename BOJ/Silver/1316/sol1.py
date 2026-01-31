# [S5] 1316 그룹 단어 체커

# STEP 1. 입력 받기
N = int(input())

cnt = 0

for _ in range(N):
    word = input()

    prev = word[0]
    visited = set(prev)

    for i in range(1, len(word)):
        if word[i] == prev:
            continue
        elif word[i] not in visited:
            visited.add(word[i])
            prev = word[i]
        else:
            break
    else:
        cnt += 1

print(cnt)