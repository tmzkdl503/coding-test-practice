'''
Title: 124 나라의 숫자
Type: 구현, 수학
Link: https://programmers.co.kr/learn/courses/30/lessons/12899
Reference: 연습문제
'''

# 0이 없기 때문에 신경써줘야 하는 문제

def convert(n, radix):
    example = '412'
    ans = ''
    
    a = n
    while True:
        q, r = divmod(a, radix)
        ans += example[r]
        if r == 0:
            q -= 1
        if q != 0:
            a = q
        else:
            break
    
    return ans[::-1]

def solution(n):
    return convert(n, 3)
