'''
Title: 나누어 떨어지는 숫자 배열
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12910
Reference: 연습문제
'''

def solution(arr, divisor):
    return sorted([x for x in arr if x % divisor == 0]) or [-1]
