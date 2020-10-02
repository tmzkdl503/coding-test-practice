'''
Title: 소수 만들기
Type: 조합, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/12977
Reference: Summer/Winter Coding(~2018)
'''

import itertools

def solution(nums):
    comb = itertools.combinations(nums, 3)
    
    eratos = [1 for _ in range(max(nums) * 3)]
    leng = len(eratos)
    for i in range(2, int(leng ** 0.5) + 1):
        if eratos[i] == 1:
            for j in range(i*2, leng, i):
                eratos[j] = 0
    
    ans = 0
    for c in comb:
        if eratos[sum(c)] == 1:
            ans += 1
            
    return ans
