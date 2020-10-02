'''
Title: 실패율
Type: 해시
Link: https://programmers.co.kr/learn/courses/30/lessons/42889
Reference: 2019 KAKAO BLIND RECRUITMENT
'''

def solution(N, stages):
    dic = {i: 0 for i in range(1, N + 2)}
    
    for stage in stages:
        dic[stage] += 1
        
    ans = []
    users = len(stages)
    
    for k, v in dic.items():
        if k == N + 1:
            break
        if users == 0:
            ans.append((k, 0))
        else:
            ans.append((k, v / users))
            users -= v
    
    return [key for key, value in sorted(ans, key=lambda x: x[1], reverse=True)]
