# [LV1] 161989 덧칠하기

def solution(n, m, section):
    answer = 0
    # wall : 벽의 페인트 정보를 담은 배열
    # 1 : 안 칠해도 됨, 0 : 칠해야 함
    wall = [1] * (n + 1)
    for num in section:
        wall[num] = 0

    # wall 순회
    # 안 칠해진 곳 있으면 그 칸 포함, m칸을 색칠
    for i in range(1, n+1):
        if wall[i] == 0:
            # 롤러 범위 확인
            if i+m <= n:
                for j in range(i, i + m):
                    wall[j] = 1
            else:
                for j in range(i, n+1):
                    wall[j] = 1
            # 페인트 칠 횟수 증가
            answer += 1
    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))