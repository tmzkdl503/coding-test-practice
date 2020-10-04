'''
Title: 스킬트리
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/49993
Reference: Summer/Winter Coding(~2018)
'''

# 상관 없는 스킬을 모두 제거한 상태로 검증하는 방법

import re

def solution(skill, skill_trees):
    ans = 0
    check = [skill[:x] for x in range(0, len(skill) + 1)]
    
    for s in list(skill_trees):

        s = re.sub(f'[^{skill}]', '', s)

        if s in check:
            ans += 1
    
    return ans
