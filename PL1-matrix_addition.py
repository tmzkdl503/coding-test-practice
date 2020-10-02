'''
Title: 행렬의 덧셈
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12950
Reference: 연습문제
'''

def solution(arr1, arr2):
    ans = []
    
    for a, b in zip(arr1, arr2):
        ans.append([x + y for x, y in zip(a, b)])
    
    return ans
