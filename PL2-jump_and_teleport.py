'''
Title: 점프와 순간 이동
Type: 구현, 로그
Link: https://programmers.co.kr/learn/courses/30/lessons/12980
Reference: Summer/Winter Coding(~2018)
'''

# 도착점부터 생각하면 2로 나누면서 나머지 만큼만 점프하면 나머지는 순간이동으로 가능

def solution(n):
    ans = 0
    
    while n > 0:
        q, r = divmod(n, 2)
        ans += r
        n = q
        
    return ans
