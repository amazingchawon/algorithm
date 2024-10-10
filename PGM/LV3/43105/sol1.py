# [LV3] 43105 정수 삼각형

def solution(triangle):
    # sum_triangle : 합을 저장할 배열
    sum_triangle = [triangle[0]] + [[0]*i for i in range(2, len(triangle)+1)]

    # 0열 - n-1열까지 순회
    # 예시의 경우, [2, 7, 4, 4]까지 순회
    for x in range(len(triangle)-1):
        for y in range(0, x+1):
            # 다음 x좌표, 왼쪽 y좌표, 오르쪽 y 좌표
            nx, ly, ry = x + 1, y, y + 1

            l_sum = sum_triangle[x][y] + triangle[nx][ly]
            if sum_triangle[nx][ly] < l_sum:
                sum_triangle[nx][ly] = l_sum

            r_sum = sum_triangle[x][y] + triangle[nx][ry]
            if sum_triangle[nx][ry] < r_sum:
                sum_triangle[nx][ry] = r_sum

    answer = max(sum_triangle[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle)) # 30