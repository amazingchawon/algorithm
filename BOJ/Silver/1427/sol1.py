# [S5] 1427 소트인사이드

str_number = input()

numbers = list(int(num) for num in str_number)
numbers.sort(reverse=True)
print(''.join(map(str, numbers)))