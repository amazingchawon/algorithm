def solution(clothes):
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
    answer = 1
    for n in items:
        answer *= n + 1
        # 해당 카테고리에서 옷을 안 고르는 경우의 수 추가

    # 옷을 하나도 안고르는 경우의 수 빼주기
    return answer - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) # 5
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes)) # 3