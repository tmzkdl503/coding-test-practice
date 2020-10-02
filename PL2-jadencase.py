'''
Title: JadenCase 문자열 만들기
Type: 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12951
Reference: 연습문제
'''

def solution(s):
    return ' '.join([x[0].upper() + x[1:].lower() if len(x) > 1 else x.upper() for x in s.split(' ')])
