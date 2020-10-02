'''
Title: N개의 최소공배수
Type: 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/12953
Reference: 연습문제
'''

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    return b if a == 0 else gcd(b%a, a)

def solution(arr):
    answer = 0
    
    a = arr[0]
    for i in range(len(arr) - 1):
        a = lcm(a, arr[i+1])
    
    return a
