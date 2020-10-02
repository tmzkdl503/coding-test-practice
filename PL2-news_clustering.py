'''
Title: 뉴스 클러스터링
Type: 구현, 문자열 처리
Link: https://programmers.co.kr/learn/courses/30/lessons/17677
Reference: 2018 KAKAO BLIND RECRUITMENT [1차]
'''

# 교집합과 합집합을 구하는 원리가 본문에 있으므로 활용

import re

def solution(str1, str2):
    set1 = []
    set2 = []
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i, c in enumerate(str1):
        if i < len(str1) - 1:
            tmp = re.sub('[^a-z]', '', c+str1[i+1])
            if len(tmp) == 2:
                set1.append(tmp)
    
    for i, c in enumerate(str2):
        if i < len(str2) - 1:
            tmp = re.sub('[^a-z]', '', c+str2[i+1])
            if len(tmp) == 2:
                set2.append(tmp)
        
    hap = 0
    kyo = 0
    for s in set(set1 + set2):
        hap += max(set1.count(s), set2.count(s))
        kyo += min(set1.count(s), set2.count(s))
        
    if hap == 0:
        return 65536
    else:
        return int(kyo / hap * 65536)
