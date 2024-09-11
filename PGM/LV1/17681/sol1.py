# [LV1] 17681 비밀지도

def solution(n, arr1, arr2):
    answer = []

    # STEP 1. 지도 합치기
    secret_map = []
    for i in range(n):
        # 이진수 or 연산으로 합치기
        check = bin(arr1[i] | arr2[i])[2:]
        # 길이가 n보다 짧은 경우, 앞에 0을 붙여주기
        length = len(check)
        if length != n:
            check = '0' * (n-length) + check
        secret_map.append(check)

    # STEP 2. 1 -> #, 0 -> (공백) 으로 변환
    for row in secret_map:
        tmp = ''
        for num in row:
            if num == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer