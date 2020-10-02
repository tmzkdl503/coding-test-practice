'''
Title: 소수 찾기
Type: 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/12921
Reference: 연습문제
'''

def solution(n):
    eratos = [1 for x in range(n + 1)] # 에라토스테네스의 체
    eratos[0], eratos[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        if eratos[i] == 1:
            for j in range(i * 2, n + 1, i):
                eratos[j] = 0
    
    return eratos.count(1)
