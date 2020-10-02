'''
Title: 제일 작은 수 제거하기
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12935
Reference: 연습문제
'''

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr
