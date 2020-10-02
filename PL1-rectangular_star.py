'''
Title: 직사각형 별찍기
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12969
Reference: 연습문제
'''

a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*' * a)
