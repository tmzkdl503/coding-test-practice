'''
Title: 콜라츠 추측
Type: 재귀
Link: https://programmers.co.kr/learn/courses/30/lessons/12943
Reference: 연습문제
'''

def cocacola(num, c):
    c += 1
    if num == 1:
        if c >= 500:
            return -1
        else:
            return c
    elif num % 2 == 0:
        return cocacola(num // 2, c) 
    else:
        return cocacola(num * 3 + 1, c)

def solution(num):
    return cocacola(num, -1)
