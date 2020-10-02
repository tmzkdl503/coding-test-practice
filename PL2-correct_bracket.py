'''
Title: 올바른 괄호
Type: 스택
Link: https://programmers.co.kr/learn/courses/30/lessons/12909
Reference: 연습문제
'''

def solution(s):
    pair = {'(': ')', ')': '('}
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            p = stack.pop()
            if c != pair[p]:
                return False
    if stack:
        return False
    return True
