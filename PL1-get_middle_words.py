'''
Title: 가운데 글자 가져오기
Type: 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12903
Reference: 연습문제
'''

def solution(s):
    L = len(s)
    return s[L // 2 - 1:L // 2+1] if L % 2 == 0 else s[L // 2]
