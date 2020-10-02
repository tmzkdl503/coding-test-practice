'''
Title: 자릿수 더하기
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12931
Reference: 연습문제
'''

def solution(n):
    return sum([int(x) for x in str(n)])
