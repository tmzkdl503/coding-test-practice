'''
Title: 직각삼각형
Type: 수학
Link: https://www.acmicpc.net/problem/4153
Reference: 수학
'''

while True:
    a, b, c = list(map(int, input().split()))
    if a == b == c == 0:
        break
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print('right')
    else:
        print('wrong')
