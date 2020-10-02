'''
Title: 예산
Type: 그리디
Link: https://programmers.co.kr/learn/courses/30/lessons/12982
Reference: Summer/Winter Coding(~2018)
'''

def solution(d, budget):
    ans = 0
    
    for a in sorted(d):
        if budget >= a:
            budget -= a
            ans += 1
        else:
            break
    
    return ans
