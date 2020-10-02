'''
Title: 압축(LZW)
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/17684
Reference: 2018 KAKAO BLIND RECRUITMENT [3차]
'''

def solution(msg):
    # 사전 초기화
    dic = [chr(ord('A')+i) for i in range(26)]
    ans = []
    
    while msg:
        found = msg[0]
        
        for i in range(len(msg)):
            if found in dic: # 사전에 있으면
                if i == len(msg) - 1: # 끝이면
                    ans.append(dic.index(found) + 1)
                    msg = ''
                    break
                else:
                    found += msg[i+1]
            else: # 사전에 없으면
                ans.append(dic.index(found[:-1]) + 1)
                dic.append(found)
                msg = msg[i:]
                break
                
    return ans
