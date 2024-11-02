# [LV3] 43162 네트워크

def solution(n, computers):
    def make_set(n):
        p = [i for i in range(n)]
        return p

    def find_set(x):
        if x == parents[x]:
            return x
        parents[x] = find_set(parents[x])
        return parents[x]

    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)

        if root_x == root_y:
            return

        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y

    parents = make_set(n)

    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                union(i, j)

    for i in range(n):
        find_set(i)
    answer = len(set(parents))
    return answer

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(n, computers)) # 2
#
# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# print(solution(n, computers)) # 1
#
# n = 1
# computers = [[1]]
# print(solution(n, computers)) # 1

n = 5
computers = [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]]
print(solution(n, computers)) # 1