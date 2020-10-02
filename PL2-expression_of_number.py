'''
Title: 숫자의 표현
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12924
Reference: 연습문제
'''

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        num = 0
        for j in range(i, n+1):
            num += j
            if num > n:
                break
            elif num == n:
                answer += 1
                break
    
    return answer
