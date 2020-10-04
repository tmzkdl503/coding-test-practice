'''
Title: 다리를 지나는 트럭
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/42583
Reference: 스택/큐
'''

# 시간을 증가시키는 시점을 헷갈리지 말자

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = truck_weights[::-1]
    bridge = deque()
    
    atime = bridge_length
    ptime = 0
    pweight = 0
    
    while truck or bridge: # 대기실이나 다리위에 하나라도 있으면 계속함
        # 만약 추가했을 때 다리 하중이 버텨진다면 새로운 트럭(있으면) 삽입, 현재 무게 증가
        if truck and pweight + truck[-1] <= weight:
            t = truck.pop()
            bridge.append([t, ptime + atime])
            pweight += t
        
        # 1초 경과
        ptime += 1
        
        # 도착 처리할(ptime == truck[1]) 트럭 있는지 체크
        if bridge[0][1] == ptime:
            tt = bridge.popleft()
            pweight -= tt[0]
    
    return ptime + 1
