'''
Title: 정수 제곱근 판별
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12934
Reference: 연습문제
'''

def solution(n):
    sq = n ** 0.5
    return (sq + 1) ** 2 if int(sq) == sq else -1
