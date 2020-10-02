'''
Title: K번째 수
Type: 정렬, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/42748
Reference: 연습문제
'''

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
