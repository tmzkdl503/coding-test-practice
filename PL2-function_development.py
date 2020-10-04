'''
Title: 기능 개발
Type: 스택, 큐
Link: https://programmers.co.kr/learn/courses/30/lessons/42586
Reference: 스택/큐
'''

# 구현으로 해결

def calc(pp, ss):
    return [p+s for p, s in zip(pp, ss)]

def solution(progresses, speeds):
    
    result = []
    
    tmp = progresses
    
    tt = 0
    
    while sum(tmp) != 0:
        t = 0
        k = 0
        for i, x in enumerate(tmp):
            if x >= 100 and k == i:
                t += 1
                k += 1
                tmp[i] = 0
                speeds[i] = 0
            elif x == 0 and k == i:
                k += 1
        if t != 0:
            result.append(t)
            
        tmp = calc(tmp, speeds)
    
    return result
