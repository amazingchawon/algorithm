# [[G5] 토마토](https://www.acmicpc.net/problem/7576)

## 연관 개념

[BFS](https://github.com/amazingchawon/TIL/blob/master/Algorithm/BFS.md)

## sol1
구현 + 완전 탐색으로 풀었어쓴데, 비효율적인 방법으로 시간초과

## sol2
- BFS로 구현
- while문 안에 반복문을 두어서 날짜별로 구분 가능하게 구현
    ```python
    while tomato:
        for _ in range(len(tomato)):
    ```