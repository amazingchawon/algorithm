# [[LV3] 43162 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

## 연관 개념
- [Union Find](https://github.com/amazingchawon/TIL/blob/master/Algorithm/Union-Find.md)

## 기억할 것
### 1. union 함수
```commandline
    def union(x, y):
        root_x = find_set(x)
        root_y = find_set(y)

        if root_x == root_y:
            return

        if root_x < root_y:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y
```
여기서 root_x를 합칠 때,
```commandline
if root_x < root_y:
    parents[y] = root_x
else:
    parents[x] = root_y
```
이렇게 적는 실수를 했다.
자신의 root노드의 parent 값을 변경해줘야 하는 걸 잊지 말기!

### 2. find_set 추가로 해주기
union 함수에서 자신의 root 노드의 값을 변경해주기 때문에, 본인이 가리키고 있는 parent가 가장 최상위 노드라고 확신할 수 없다.따라서 마지막에 find_set을 한번 더 실행해 주어야 한다.

