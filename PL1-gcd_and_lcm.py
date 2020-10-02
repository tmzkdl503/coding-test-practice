'''
Title: 최대공약수와 최소공배수
Type: 재귀, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/12940
Reference: 연습문제
'''

# 유클리드 호제법
def gcd(a, b):
    return b if a == 0 else gcd((b % a), a)

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
