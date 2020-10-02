'''
Title: 정수 내림차순으로 배치하기
Type: 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/12933
Reference: 연습문제
'''

def solution(n):
    # 문자열을 정렬하면 리스트가 되므로 다시 문자열로 재변환
    return int(''.join(sorted(str(n), reverse=True)))
