'''
Title: 약수의 합
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12928
Reference: 연습문제
'''

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    
    return answer
