'''
Title: 예상 대진표
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12985
Reference: 2017 팁스다운
'''

# 프랙탈 구조가 보이므로 재귀적 원리를 활용

def solution(n,a,b):
    answer = 0

    while a != b:
        # 계산 편의를 위해 항상 짝수로 보정
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        answer += 1
        
    return answer
