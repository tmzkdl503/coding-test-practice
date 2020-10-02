'''
Title: 위장
Type: 해시, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/42578
Reference: 해시
'''

# 등식 표현을 활용
# a + b + ab + 1== (a+1)(b+1)
# a+b+c+ab+bc+ca+abc+1 = (a+1)(b+1)(c+1)

import collections

def solution(clothes):
    ans = 0
    
    dic = collections.defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1
    
    cnt = 1
    for i in dic.values():
        cnt *= (i+1)
    return cnt - 1
