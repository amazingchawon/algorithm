# [[D4] 쇠막대기 자르기](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZCW2rDqGb4DFAUC&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AZCW3xNaGdQDFAUC&type=PROBLEM&problemBoxTitle=%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4+I&problemBoxCnt=10)

## sol1
쇠막대기를 레이저로 나눈다는 문제의 상황을 문자 그대로 받아들여 스택을 여러개 만들어서 풀이했다. 그랬더니 런타임 에러가 났다.

## sol2
레이저를 따로 구분하지 않았다. 여는 괄호, 닫는 괄호가 연달아 들어오는 상황과, 아닌 상황을 구분하여 풀었다. 주어진 문자열을 1번만 반복해서 푸는 방식으로 구현했다.

## sol3
스택을 사용하지 않고 풀었다. 스택에 들어가는 것은 여는 괄호 뿐이니, 내용물은 중요하지 않았고 스택의 현재 길이만 필요하여 cnt 변수로 대신하였다.