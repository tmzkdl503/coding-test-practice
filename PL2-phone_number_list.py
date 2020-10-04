'''
Title: 전화번호 목록
Type: 해시
Link: https://programmers.co.kr/learn/courses/30/lessons/42577
Reference: 해시
'''

import re

def solution(phone_book):
    answer = True
    
    for p in phone_book:
        for q in phone_book:
            if p != q:
                if re.findall(f'^{p}', q): # ^는 접두어를 의미, f는 문자열에 변수 배정 가능
                    return False
    
    return answer
