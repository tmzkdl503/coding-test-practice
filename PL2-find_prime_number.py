'''
Title: 소수 찾기
Type: 브루트포스, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/42839
Reference: 완전탐색
'''

import itertools

def powerset(s):
    length = len(s)
    return itertools.chain.from_iterable(itertools.permutations(s, r) for r in range(length + 1))

def solution(numbers):
    ans = 0
    
    big = int(''.join(sorted(numbers, reverse=True)))
    eratos = [x for x in range(big+1)]
    
    for i in range(2, big+1):
        if eratos[i]:
            for j in range(i*2, big+1, i):
                eratos[j] = False
    eratos[0] = eratos[1] = False
            
    tmp = {int(''.join(list(x))) for x in powerset(list(numbers)) if x}
    
    for q in list(tmp):
        if q:
            print(eratos[q], q)
            if eratos[q]:
                ans += 1
    
    return ans
