'''
Title: 크레인 인형뽑기 게임
Type: 구현, 스택
Link: https://programmers.co.kr/learn/courses/30/lessons/64061
Reference: 2019 카카오 개발자 겨울 인턴십
'''

def solution(board, moves):
    stack = []
    height = len(board)
    count = 0
    
    for m in moves:
        col = m - 1
        
        for i in range(height):
            if board[i][col] != 0: # 뭔가 주움
                if stack and stack[-1] == board[i][col]: # 스택 맨 위랑 같으면 제거하고 카운트
                    board[i][col] = 0
                    stack.pop()
                    count += 2
                    break
                else: # 새로우면 스택에 추가
                    stack.append(board[i][col])
                    board[i][col] = 0
                    break
                
    return count
