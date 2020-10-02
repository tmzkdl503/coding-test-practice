'''
Title: 두 개 뽑아서 더하기
Type: 조합, 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/68644
Reference: 월간 코드 챌린지 시즌1
'''

import itertools

def solution(numbers):
    ans = set()
    
    comb = itertools.combinations(numbers, 2)
    
    for a, b in comb:
        ans.add(a + b)
        
    return sorted(list(ans))
