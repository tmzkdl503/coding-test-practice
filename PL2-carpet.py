'''
Title: 카펫
Type: 완전탐색, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/42842
Reference: 연습문제
'''

def solution(brown, yellow):
    _sum = brown // 2 - 2
    _mul = yellow
    
    sample = [[_sum - x, x] for x in range(1, _sum)]
    
    for s in sample:
        if s[0] * s[1] == _mul:
            return [s[0]+2, s[1]+2]
