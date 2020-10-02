'''
Title: 다트 게임
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/17682
Reference: 2018 KAKAO BLIND RECRUITMENT [1차]
'''

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}

    # 정규 표현식에서 ()로 그룹화 하면 각 그룹 단위로 튜플을 만듦
    # 예시 입력값: 1S2D*3T
    # 그룹화 미사용 시: ['1S', '2D*', '3T']
    # 그룹화 사용 시: [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    dart = re.findall('(\d+)([SDT])([*#]?)', dartResult)
    
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    return sum(dart)
