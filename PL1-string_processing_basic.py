'''
Title: 문자열 다루기 기본
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12918
Reference: 연습문제
'''

def solution(s):
    return True if len(s) in (4, 6) and s.isdigit() else False
