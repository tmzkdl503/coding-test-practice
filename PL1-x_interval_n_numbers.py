'''
Title: x만큼 간격이 있는 n개의 숫자
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12954
Reference: 연습문제
'''

def solution(x, n):
    return [x * i for i in range(1, n + 1)]
