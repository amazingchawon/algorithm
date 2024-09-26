# [LV2] 258711 도넛과 막대 그래프

def solution(edges):
    # STEP 1. 인접리스트 만들기
    # 정점 번호 중 가장 큰거 찾기
    vertax_num = max(map(max, edges))
    adj = [[] for _ in range(vertax_num+1)]

    # check_vertax : 추가된 정점이 무엇인지 확인하기 위한 배열, 정점으로 들어오는 간선 수를 셈
    # 0번 정점은 존재하지 않으니 -1로 초기화
    check_vertax = [-1] + [0] * vertax_num

    for edge in edges:
        start, end = edge
        # end 정점에 들어오는 간선 수 증가
        check_vertax[end] += 1
        # 인접리스트에 정점 추가
        adj[start].append(end)

    # STEP 2. 추가된 정점, 막대 그래프 수, 8자 그래프 수 찾기
    stick = 0
    eight = 0

    for i in range(1, vertax_num+1):
        # 해당 정점에서 간선이 없다 == 막대 그래프의 마지막 점
        # 막대 그래프의 마지막 정점의 개수 == 막대 그래프의 개수
        if len(adj[i]) == 0 and check_vertax[i] >= 1:
            stick += 1
        # 8자 그래프 수 세기
        # 8자 그래프 중심 == 나가는 간선 2개 and 들어오는 간선 2개
        elif len(adj[i]) == 2 and check_vertax[i] >= 2:
            eight += 1
        # 추가된 정점 찾기
        # 추가된 정점 == 나가는 간선 2개 이상 and 들어오는 간선 0개
        elif len(adj[i]) >=2 and check_vertax[i] == 0:
            vertax_added = i

    # STEP 3. 도넛 그래프 수 계산
    # total : 그래프 수, 추가한 정점에서 연결된 간선 수와 같음
    total = len(adj[vertax_added])

    # 도넛 그래프 수
    # 전체 그래프 - 막대 - 8자
    donut = total - stick - eight

    answer = [vertax_added, donut, stick, eight]
    return answer

# [2, 1, 1, 0]
# print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
# [4, 0, 1, 2]
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))