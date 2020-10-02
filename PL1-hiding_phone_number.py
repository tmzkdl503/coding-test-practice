'''
Title: 핸드폰 번호 가리기
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/12948
Reference: 연습문제
'''

def solution(phone_number):
    return ''.join(['*' for _ in range(len(phone_number) - 4)]) + phone_number[-4:]
