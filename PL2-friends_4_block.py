'''
Title: 프렌즈4블록
Type: 구현, 브루트포스
Link: https://programmers.co.kr/learn/courses/30/lessons/17679
Reference: 2018 KAKAO BLIND RECRUITMENT [1차]
'''

def solution(m, n, board):
    board = [list(x) for x in board]
    ans = 0
    
    while True:
        # 터뜨리기
        boom = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '@':
                    boom.add((i, j))
                    boom.add((i+1, j))
                    boom.add((i, j+1))
                    boom.add((i+1, j+1))
                    
        ans += len(boom)
        for i, j in boom:
            board[i][j] = '@'
        
        if not boom: # 터질 폭탄이 없으면 종료
            break
        
        # 끌어내리기
        for j in range(n):
            for _ in range(m-1):
                for i in range(m-1):
                    if board[i][j] != '@' and board[i+1][j] == '@':
                        board[i+1][j] = board[i][j]
                        board[i][j] = '@'
                        
    return ans
