'''
Title: 시저 암호
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12926
Reference: 연습문제
'''

def solution(s, n):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lo = up.lower()
    
    answer = ''
    
    for c in s:
        if c == ' ':
            answer += ' '
        elif c.isupper():
            answer += up[(up.find(c) + n) % 26]
        else:
            answer += lo[(lo.find(c) + n) % 26]
            
    return answer
