# [LV3] 42861 섬 연결하기

def solution(n, costs):
    answer = 0

    # 섬 연결 저장할 배열
    arr = [[] * n for _ in range(n)]

    # costs 비용 순으로 정렬
    costs.sort(key=lambda x: x[2])

    connections = [{costs[0][0], costs[0][1]}]
    extras = []

    # STEP 1. 연결 저장
    for data in costs:
        start, end, cost = data
        if len(arr[start]) == 0 or len(arr[end]) == 0:
            arr[start].append(end)
            arr[end].append(start)
            for i in range(len(connections)):
                if (start in connections[i]) or (end in connections[i]):
                    connections[i].add(start)
                    connections[i].add(end)
                    break
                else:
                    connections.append({start, end})
            answer += cost
        else:
            extras.append(data)

    # STEP 2. 다 연결되었는지 확인
    idx = 0
    start_check = -1
    end_check = -1
    while len(connections) != 1:
        start, end, cost = extras[idx]
        for i in range(len(connections)):
            if start in connections[i] and end in connections[i]:
                continue
            elif start in connections[i] and end not in connections[i]:
                start_check = i
            elif start not in connections[i] and end in connections[i]:
                end_check = i
            if start_check != -1 and end_check != -1:
                connections[start_check] = set.union(connections[start_check], connections[end_check])
                connections.pop(end_check)
                answer += cost

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs)) # 4

n = 6
costs = [[0, 1, 3], [0, 2, 4], [1, 3, 8], [1, 4, 1], [1, 5, 5], [2, 3, 1], [3, 4, 4], [4, 5, 2]]
print(solution(n, costs)) # 11