'''
Title: 파일명 정렬
Type: 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/17686
Reference: 2018 KAKAO BLIND RECRUITMENT [3차]
'''

import re

def solution(files):
    a = []

    for file in files:
        tmp = re.findall('([^0-9]+)([0-9]{1,5})(.*)', file)
        a.append((file, *tmp))
    
    a.sort(key=lambda x: (x[1][0].lower(), int(x[1][1])))
    
    return [x[0] for x in a]
