# [LV2] 42860 조이스틱
# 실패
def solution(name):
    answer = 0
    # 주어진 글자 수 카운트
    length = len(name)
    left = ['A'] * length
    right = ['A'] * length

    # STEP 1. 첫번째 자리 바꾸기
    # A -> B 방향으로 이동 횟수
    forward = ord(name[0]) - 65
    # A -> Z 방향으로 이동 횟수
    backward = 90 - ord(name[0]) + 1
    answer += min(forward, backward)
    # 실제로 글자를 변경
    right[0] = name[0]
    left[0] = name[0]
    # 다음으로 커서 이동
    answer += 1
    right_cnt = answer
    left_cnt = answer

    # STEP 2. 순회 : 오른쪽으로, 왼쪽으로 순회 비교해서 적은걸로!
    # 커서를 오른쪽으로 이동
    for i in range(1, length):
        # A -> B 방향으로 이동 횟수
        forward = ord(name[i]) - 65
        # A -> Z 방향으로 이동 횟수
        backward = 90 - ord(name[i]) + 1
        right_cnt += min(forward, backward)
        # 실제로 글자를 변경
        right[i] = name[i]
        # 그 다음으로 커서 이동
        right_cnt += 1
        # 현재 문자열 상태와 정답과 비교 -> 같으면 break
        if ('').join(right) == name:
            break

    # 커서를 왼쪽으로 이동
    for j in range(-1, -(length), -1):
        # A -> B 방향으로 이동 횟수
        forward = ord(name[j]) - 65
        # A -> Z 방향으로 이동 횟수
        backward = 90 - ord(name[j]) + 1
        left_cnt += min(forward, backward)
        # 실제로 글자를 변경
        left[j] = name[j]
        # 그 다음으로 커서 이동
        left_cnt += 1
        # 현재 문자열 상태와 정답과 비교 -> 같으면 break
        if ('').join(left) == name:
            break

    answer = min(left_cnt-1, right_cnt-1)
    return answer

# name = "JEROEN"
# print(solution(name))

name = "ABBAAABAAAABB"
print(solution(name))