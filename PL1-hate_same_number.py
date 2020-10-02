'''
Title: 같은 숫자는 싫어
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12906
Reference: 연습문제
'''

# 같은 숫자가 중복되어 뒤에 나올 수 있으므로 딕셔너리를 쓸 수 없음
def solution(arr):
    ans = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
    
    return ans
