'''
Title: 완주하지 못한 선수
Type: 구현, 해시
Link: https://programmers.co.kr/learn/courses/30/lessons/42576
Reference: 해시
'''

# Counter 객체는 key, count를 쌍으로 가지며 덧셈 뺄셈이 가능함
import collections

def solution(participant, completion):
    v1 = collections.Counter(participant) - collections.Counter(completion)
    return list(v1.keys())[0]
