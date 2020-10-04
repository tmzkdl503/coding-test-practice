'''
Title: 괄호 변환
Type: 구현, 스택
Link: https://programmers.co.kr/learn/courses/30/lessons/60058
Reference: 2020 KAKAO BLIND RECRUITMENT
'''

import sys

sys.setrecursionlimit(10 ** 8)

sett = {'(': ')', ')': '('}

def check(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack or sett[c] != stack.pop():
                return False
    return True

def solution(p):
    if not p:
        return ''
    le = 0
    ri = 0
    u = ''
    v = ''
    for c in p: # u, v로 나눔
        if le != 0 and le == ri:
            v += c
        else:
            if c == '(':
                u += c
                le += 1
            else:
                u += c
                ri += 1
    if check(u): # u가 올바른 문자열이라면
        return u + solution(v)
    else: # 아니라면
        tmp = '(' + solution(v) + ')'
        u = u[1:-1]
        for c in u:
            tmp += sett[c]
        return tmp
