'''
Title: 두 정수 사이의 합
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12912
Reference: 연습문제
'''

def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))
