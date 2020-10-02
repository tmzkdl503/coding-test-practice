'''
Title: 오픈채팅방
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/42888
Reference: 2019 KAKAO BLIND RECRUITMENT
'''

# id를 딕셔너리로 관리하고 모든 과정이 끝난 뒤 id를 닉네임으로 치환해 줌

import collections

def solution(record):
    result = []
    userlist = {}
    userindex = collections.defaultdict(list)
    
    pos = -1
    
    for index, log in enumerate(record):
        token = log.split(' ')
        
        if token[0][0] == 'E': # Enter
            pos += 1
            result.append(f'{token[1]}님이 들어왔습니다.')
            userlist[token[1]] = token[2]
            userindex[token[1]].append(pos)
        elif token[0][0] == 'L': # Leave
            pos += 1
            result.append(f'{token[1]}님이 나갔습니다.')
            userindex[token[1]].append(pos)
        elif token[0][0] == 'C': # Change
            userlist[token[1]] = token[2]
            
    for uid, poslist in userindex.items():
        for pos in poslist:
            result[pos] = result[pos].replace(uid, userlist[uid])
    
    return result
