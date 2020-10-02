'''
Title: 하샤드 수
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12947
Reference: 연습문제
'''

def solution(x):
    return x % sum([int(a) for a in str(x)]) == 0
