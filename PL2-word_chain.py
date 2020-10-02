'''
Title: 영어 끝말잇기
Type: 구현
Link: https://programmers.co.kr/learn/courses/30/lessons/12981
Reference: Summer/Winter Coding(~2018)
'''

def solution(n, words):
    prev = []
    
    for i, word in enumerate(words):
        count = i // n + 1
        if word in prev or (i != 0 and words[i-1][-1] != word[0]):
            return [i % n + 1, count]
        prev.append(word)
