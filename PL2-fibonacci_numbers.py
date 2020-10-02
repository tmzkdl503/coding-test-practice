'''
Title: 피보나치 수
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12945
Reference: 연습문제
'''

def solution(n):
    pibb = [0, 1]
    
    for i in range(2, n+1):
        pibb.append(pibb[i-2] + pibb[i-1])
        
    return pibb[n] % 1234567
