def solution(clothes):
    answer = 0
    closet = {}

    # STEP 1. 딕셔너리 만들기
    for val, key in clothes:
        if key in closet:
            closet[key] += 1
        else:
            closet[key] = 1

    items = list(closet.values())

    cases = []

    # STEP 2. 경우의 수 세기
    for i in range(1 << len(closet)):
        tmp = 1
        check = 0
        for idx in range(len(closet)):
            if i & (1 << idx):
                check = 1
                tmp *= items[idx]
        if check:
            answer += tmp

    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) # 5
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes)) # 3