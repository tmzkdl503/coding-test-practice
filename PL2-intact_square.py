'''
Title: 멀쩡한 사각형
Type: 구현, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/62048
Reference: Summer/Winter Coding(2019)
'''

# 수학적인 방법

def gcd(a, b):
    return b if a == 0 else gcd((b % a), a)

def solution(w, h):
    return w*h - w -h + gcd(w, h)
