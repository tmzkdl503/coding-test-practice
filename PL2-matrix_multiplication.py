'''
Title: 행렬의 곱셈
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12949
Reference: 연습문제
'''

def solution(arr1, arr2):
    ans = []
    arr2 = [list(x) for x in zip(*arr2)]
    
    for a1 in arr1:
        tmp = []
        for a2 in arr2:
            t = 0
            for aa, bb in zip(a1, a2):
                t += aa*bb    
            tmp.append(t)
        ans.append(tmp)

    return ans
