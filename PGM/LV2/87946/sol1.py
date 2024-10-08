# [LV2] 87946 피로도

# 순열 만들기
def perm(length):
    chosen = []
    used = [0] * length
    perms = []

    def generate(chosen, used):
        if len(chosen) == length:
            perms.append(chosen[:])
            return

        for num in range(length):
            if used[num] == 0:
                chosen.append(num)
                used[num] = 1
                generate(chosen, used)
                used[num] = 0
                chosen.pop()
    generate(chosen, used)
    return perms

def solution(k, dungeons):
    answer = -1
    # number : 던전 수
    number = len(dungeons)
    # orders : 던전 순회 순서 저장할 배열
    orders = perm(number)

    # order 순회 -> 순서대로 던전 순회하면서 최대로 많이 돌 수 있는 던전 수 갱신하기
    for order in orders:
        # hp : 현재 피로도 기록 변수, cnt : 방문 던전 수 기록 변수
        hp = k
        cnt = 0
        for idx in order:
            hp_required, hp_consume = dungeons[idx]
            # 던전 방문 가능한 경우 = 해당 던전의 최소 필요 피로도가 현재 피로도보다 작거나 같은 경우
            if hp >= hp_required:
                # 피로도 감소, 방문 던전 수 갱신
                hp -= hp_consume
                cnt += 1
        # 현재 순서대로 방문했을 때 방문 던전 수 VS 이전에 저장된 방문 던전 수
        if answer <= cnt:
            answer = cnt

    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))   # 3