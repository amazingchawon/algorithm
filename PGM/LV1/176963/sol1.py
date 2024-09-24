# [LV1] 176963 추억 점수

def solution(name, yearning, photo):
    answer = [0] * len(photo)

    # 사진 1장씩 살펴보기
    for i in range(len(photo)):
        # pic : 사진에 포함된 사람들을 저장한 배열
        pic = photo[i]

        # pic 순회 -> 사진에 누가 있나!
        for person in pic:
            # 그리운 사람이면,
            if person in name:
                # answer 배열에 그리움 점수 추가
                answer[i] += yearning[name.index(person)]
    return answer