'''
Title: 더 맵게
Type: 힙
Link: https://programmers.co.kr/learn/courses/30/lessons/42626
Reference: 힙
'''

import heapq

def solution(scoville, K):
    
    heap = []
    
    for sc in scoville:
        heapq.heappush(heap, sc)
    
    count = 0
    
    while True:
        sc1 = heapq.heappop(heap)
        if sc1 >= K:
            break
        else:
            if not heap:
                count = -1
                break
                
            sc2 = heapq.heappop(heap)
            
            sc3 = sc1 + (sc2 * 2)
            count += 1
            heapq.heappush(heap, sc3)
    
    return count
