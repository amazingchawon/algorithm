# [LV2] 17677 뉴스 클러스터링

def solution(str1, str2):
    A = []
    B = []
    # STEP 1. 2글자씩 끊어서, 공백/숫자 제외, 대문자로 변환
    for i in range(0, len(str1)-1):
        char1, char2 = str1[i], str1[i+1]
        ascii1, ascii2 = ord(char1), ord(char2)
        if (65 <= ascii1 <= 90 or 97 <= ascii1 <= 122) and (65 <= ascii2 <= 90 or 97 <= ascii2 <= 122):
            A.append(char1.upper()+char2.upper())
    for i in range(0, len(str2)-1):
        char1, char2 = str2[i], str2[i + 1]
        ascii1, ascii2 = ord(char1), ord(char2)
        if (65 <= ascii1 <= 90 or 97 <= ascii1 <= 122) and (65 <= ascii2 <= 90 or 97 <= ascii2 <= 122):
            B.append(char1.upper()+char2.upper())

    # STEP 2. 자카드 유사도 계산
    intersection = {}
    union = dict(map(lambda x: [x, max(A.count(x), B.count(x))], set(A+B)))

    for word in A:
        # A, B 둘다에 있다
        if word in B:
            intersection[word] = min(A.count(word), B.count(word))  # 합집합에는 둘 중 작은 개수

    if sum(union.values()) == 0:
        answer = 65536
    else:
        check1 = sum(intersection.values())
        check2 = sum(union.values())
        check3 = check1 / check2
        check4 = check3 * 65536
        check5 = int(check4)
        answer = int((sum(intersection.values()) / sum(union.values())) * 65536)
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))