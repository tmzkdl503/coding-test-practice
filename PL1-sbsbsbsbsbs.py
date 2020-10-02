'''
Title: 수박수박수박수박수박수?
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12922
Reference: 연습문제
'''

def solution(n):
    text = '수박'
    ans = ''
    
    for i in range(n):
        ans += text[i % 2]
        
    return ans
