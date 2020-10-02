'''
Title: 땅따먹기
Type: 다이나믹 프로그래밍
Link: https://programmers.co.kr/learn/courses/30/lessons/12913
Reference: 연습문제
'''

def solution(land):
    n = len(land)
    
    D = [[0, 0, 0, 0] for _ in range(n)]
    D[0] = land[0]
    
    for i in range(1, n):
        D[i] = [
            max(D[i-1][1], D[i-1][2], D[i-1][3]) + land[i][0],
            max(D[i-1][0], D[i-1][2], D[i-1][3]) + land[i][1],
            max(D[i-1][0], D[i-1][1], D[i-1][3]) + land[i][2],
            max(D[i-1][0], D[i-1][1], D[i-1][2]) + land[i][3],
        ]  
    
    return max(D[n-1])
