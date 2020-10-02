'''
Title: 문자열 내 마음대로 정렬하기
Type: 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/12915
Reference: 연습문제
'''

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
