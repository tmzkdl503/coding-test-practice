'''
Title: 튜플
Type: 집합
Link: https://programmers.co.kr/learn/courses/30/lessons/64065
Reference: 2019 카카오 개발자 겨울 인턴십
'''

def solution(s):
    g1 = s[2:-2].split('},{')
    g2 = sorted([set(x.split(',')) for x in g1], key=len)
    
    ans = [int(list(g2[0])[0])]
    for i in range(1, len(g2)):
        ans.append(int(list(g2[i]-g2[i-1])[0]))
        
    return ans
