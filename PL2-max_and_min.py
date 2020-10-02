'''
Title: 최댓값과 최솟값
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12939
Reference: 연습문제
'''

def solution(s):
    ss = [int(x) for x in s.split(' ')]
    return str(min(ss)) + ' ' + str(max(ss))
