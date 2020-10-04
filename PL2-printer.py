'''
Title: 프린터
Type: 스택, 큐
Link: https://programmers.co.kr/learn/courses/30/lessons/42587
Reference: 스택/큐
'''

from collections import deque

def solution(priorities, location):
    answer = 0
    
    new = [(x, i) for i, x in enumerate(priorities)]
    new = deque(new)
    count = 0
    
    while new:
        g = new.popleft()
        flag = 0
        for p in new:
            if g[0] < p[0]:
                new.append(g)
                flag = 1
                break
        if flag == 0:
            count += 1
            if g[1] == location:
                answer = count
                break
    
    return answer
