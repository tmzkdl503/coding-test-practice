'''
Title: 가장 큰 수
Type: 정렬
Link: https://programmers.co.kr/learn/courses/30/lessons/42746
Reference: 정렬
'''

def solution(numbers):
    first = [str(x) for x in numbers]
    first.sort(key=lambda x: x*3, reverse=True) # 문자열을 3번 반복하여 사전 역순으로 배열하는 방법

    return str(int(''.join(first)))
