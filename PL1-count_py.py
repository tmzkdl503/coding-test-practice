'''
Title: 문자열 내 p와 y의 개수
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12916
Reference: 연습문제
'''

def solution(s):
    low = s.lower()
    return True if low.count('p') == low.count('y') else False
