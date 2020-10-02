'''
Title: 캐시
Type: 구현, 큐
Link: https://programmers.co.kr/learn/courses/30/lessons/17680
Reference: 2018 KAKAO BLIND RECRUITMENT [1차]
'''

import collections

def solution(cacheSize, cities):
    cache = collections.deque() # 오른쪽부터 들어오고 왼쪽부터 꺼내는 큐
    time = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        _city = city.lower()
        if _city in cache: # 캐시에 있는데 불리면 맨 후순위로 재배치
            cache.remove(_city)
            cache.append(_city)
            time += 1
        else: # 캐시에 없으면(miss)
            if len(cache) < cacheSize:
                cache.append(_city)
                time += 5
            else:
                cache.popleft()
                cache.append(_city)
                time += 5
            
    return time
