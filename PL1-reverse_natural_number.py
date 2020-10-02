'''
Title: 자연수 뒤집어 배열로 만들기
Type: 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/12932
Reference: 연습문제
'''

def solution(n):
    return [int(x) for x in str(n)][::-1]
