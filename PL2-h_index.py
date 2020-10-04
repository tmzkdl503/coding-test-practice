'''
Title: H-Index
Type: 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/42747
Reference: 정렬
'''

def solution(citations):
    citations.sort()
    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
            
    return 0
