# [[S3] 1149 RGB거리](https://www.acmicpc.net/problem/1149)

## 연관 개념

[DP](https://github.com/amazingchawon/TIL/blob/master/Algorithm/DP.md)

## 풀이 설명

i번쨰 집까지 칠하는데 최소 비용은
```commandline
i번째 집이 R : i-1번째 집이 G색 일 경우 or B색 일 경우
i번째 집이 G : i-1번째 집이 R색 일 경우 or B색 일 경우
i번쨰 집이 B : i-1번째 집이 R색 일 경우 or G색 일 경우
```
이 세가지 경우의 수 중 가장 작은 것이다.