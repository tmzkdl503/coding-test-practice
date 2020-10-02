'''
Title: 비밀지도
Type: 비트 연산
Link: https://programmers.co.kr/learn/courses/30/lessons/17681
Reference: 2018 KAKAO BLIND RECRUITMENT [1차]
'''

def solution(n, arr1, arr2):
    add = [bin(x | y)[2:] for x, y in zip(arr1, arr2)]
    return [' ' * (n - len(a)) + a.replace('0', " ").replace('1', '#') for a in add]
