'''
Title: 이상한 문자 만들기
Type: 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12930
Reference: 연습문제
'''

def solution(s):
    answer = ''
    count = 0
    
    for i, c in enumerate(s):
        if c == ' ':
            answer += ' '
            count = 0
        elif count % 2 == 0:
            answer += c.upper()
            count += 1
        else:
            answer += c.lower()
            count += 1
            
    return answer
