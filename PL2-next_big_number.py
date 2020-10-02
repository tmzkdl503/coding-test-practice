'''
Title: 다음 큰 숫자
Type: 구현, 비트
Link: https://programmers.co.kr/learn/courses/30/lessons/12911
Reference: 연습문제
'''

def solution(n):
    bn = list(bin(n)[2:])
    while True:
        n += 1
        nbn = list(bin(n)[2:])
        
        if bn.count('1') == nbn.count('1'):
            return n
