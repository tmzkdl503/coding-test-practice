'''
Title: 후보키
Type: 구현, 집합
Link: https://programmers.co.kr/learn/courses/30/lessons/42890
Reference: 2019 KAKAO BLIND RECRUITMENT
'''

# 성질 2개를 한번에 체크하는 방법도 있음(issubset 함수 활용)

import itertools

def powerset(somelist):
    return itertools.chain.from_iterable(itertools.combinations(somelist, x) for x in range(1, len(somelist) + 1))

def solution(relation):
    # 1. 유일성
    # 2. 최소성

    # 값은 동일한데 속성이 다른 경우를 구별하기 위해 각 값 끝에 속성 인덱스 번호를 concat해줌
    rotate = [tuple(map(lambda a: a + str(i), x)) for i, x in enumerate(zip(*relation))]

    pwset = powerset(rotate)

    # 1. 유일성
    entry = set()

    for s in pwset:
        tmp = [x for x in zip(*s)]
        if len(tmp) == len(set(tmp)):
            entry.add(s)

    # 2. 최소성
    exc = set()

    for e1 in entry:
        for e2 in entry:
            if e1 != e2 and set(e1) & set(e2) == set(e1):
                exc.add(e2)

    return len(entry - exc)
