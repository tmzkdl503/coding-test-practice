'''
Title: 모의고사
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/42840
Reference: 연습문제
'''

def solution(answers):
    p0 = [1, 2, 3, 4, 5]
    p1 = [2, 1, 2, 3, 2, 4, 2, 5]
    p2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == p0[i % len(p0)]:
            score[0] += 1
        if ans == p1[i % len(p1)]:
            score[1] += 1
        if ans == p2[i % len(p2)]:
            score[2] += 1
    
    return [i + 1 for i, s in enumerate(score) if s == max(score)]
