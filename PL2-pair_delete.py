'''
Title: 짝지어 제거하기
Type: 스택
Link: https://programmers.co.kr/learn/courses/30/lessons/12973
Reference: 2017 팁스다운
'''

def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack or stack[-1] != s[i]:
            stack.append(s[i])
        else:
            stack.pop()
    if stack:
        return 0
    else:
        return 1
