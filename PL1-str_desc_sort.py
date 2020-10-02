'''
Title: 문자열 내림차순으로 배치하기
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12917
Reference: 연습문제
'''

import re

def solution(s):
    up = ''.join(sorted(re.sub(r'[^A-Z]', '', s), reverse=True))
    lo = ''.join(sorted(re.sub(r'[^a-z]', '', s), reverse=True))
    
    return lo + up
