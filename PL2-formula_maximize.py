'''
Title: 수식 최대화
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/67257
Reference: 2020 카카오 인턴십
'''

import re
import itertools

def solution(expression):
    # re.split()에서 그룹화를 쓰면 구분자를 생략하지 않고, 쓰지 않으면 생략
    exp = re.split('([-+*])', expression)
    
    ops = itertools.permutations(['-','+','*'], 3)
    ans = set()
    
    for op in ops:
        ex = exp[:]
        for o in op:
            while o in ex:
                i = ex.index(o)
                tmp = str(eval(ex[i-1] + o + ex[i+1]))
                ex[i-1] = tmp
                del ex[i:i+2]
        ans.add(abs(int(ex[0])))
                
    return max(ans)
