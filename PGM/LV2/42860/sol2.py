# [LV2] 42860 조이스틱
# 성공
def solution(name):
    answer = 0
    # 주어진 글자 수 카운트
    length = len(name)
    # 오른쪽 방향으로 이동하면 몇번 이동해야하는지 저장히는 배열
    right = []
    # 왼쪽 방향으로 이동하면 몇번 이동해야하는지 저장하는 배열
    left = []

    # STEP 1. 알파벳 바꾸기
    for idx in range(length):
        if name[idx] != 'A':
            # A -> B 방향으로 이동 횟수
            forward = ord(name[idx]) - 65
            # A -> Z 방향으로 이동 횟수
            backward = 90 - ord(name[idx]) + 1
            answer += min(forward, backward)
            # 첫번째는 A가 아니더라도 이동할 필요가 없으니까 뺴주기
            if idx != 0:
                right.append(idx)
                left.append(length-idx)

    # STEP 2. 순회
    # 만약 A가 한개도 없다면, 그냥 오른쪽으로 쑥 가면 최소!
    if name.count('A') == 0:
        answer += right[-1]
    # 만약 모두 A라면
    elif len(right) == 0 and len(left) == 0:
        return answer
    else:
        left_cnt = 0
        right_cnt = 0
        # right과 left를 비교해서 둘이 반전되는 곳을 찾기
        for i in range(len(right)):
            if right[i] <= left[i]:
                right_cnt = right[i]
            else:
                left_cnt = left[i]
                break

        # 왼쪽으로 가다가 빽해서 오른쪽으로 가기 VS 오른쪽으로 가다가 빽 해서 왼쪽으로 가기
        if right_cnt > left_cnt:
            move = right_cnt + left_cnt * 2
        else:
            move = right_cnt * 2 + left_cnt

        # move VS 오른쪽으로 쭉 VS 왼쪽으로 쭉
        if move < min(right[-1], left[0]):
            answer += move
        else:
            answer += min(right[-1], left[0])
    return answer

# name = "JEROEN"
# print(solution(name)) # 56
#
# name = "JAN"
# print(solution(name)) # 23

# name = "ABBAAABAAAABB"
# print(solution(name)) # 15

# name = "BBBBAAAABA"
# print(solution(name)) # 12
#
# name = "AAA"
# print(solution(name)) # 0
#
# name = "AAB"
# print(solution(name)) # 2
#
# name = "AAAAAAAAABBBBB"
# print(solution(name)) # 10
#
# print(solution("ABAAAAAAAAABB")) # 7
# print(solution("BBBBAAAAAB")) # 10
# print(solution("BBBBAAAABA")) # 12
#
# name = "AAABBAAAABBAAAAAAA"
# print(solution(name)) # 14

name = "ZAAAZZZZZZZ"
print(solution(name)) # 15