'''
Title: 폰켓몬
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/1845
Reference: 찾아라 프로그래밍 마에스터
'''

def solution(nums):
    return min(len(set(nums)), len(nums)//2)
