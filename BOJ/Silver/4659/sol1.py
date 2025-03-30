# [S5] 4659 비밀번호 발음하기

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()

    # 종료 조건
    if password == 'end':
        break

    is_acceptable = True

    # 조건 1. 모음이 없을 경우 불가
    if not any(vowel in password for vowel in vowels):
        is_acceptable = False

    # 조건 2. 3개 연속 모음or자음 불가
    cnt_v, cnt_c = 0, 0
    for char in password:
        if char in vowels:
            cnt_v += 1
            cnt_c = 0
        else:
            cnt_v = 0
            cnt_c += 1

        if cnt_v == 3 or cnt_c == 3:
            is_acceptable = False
            break

    # 조건 3. 같은 글자 연속 2번 불가 (ee, oo 제외)
    for i in range(1, len(password)):
        if password[i-1] == password[i] and password[i] not in {'e', 'o'}:
            is_acceptable = False
            break

    if is_acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')