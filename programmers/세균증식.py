import sys
sys.setrecursionlimit(100000)

def check(x,y,board,max_virus,rows,columns):
    #위
    if x > 0 :
        if board[x-1][y]<max_virus:
            board[x-1][y]+=1
        else : 
            check(x-1,y,board,max_virus,rows,columns)
            
    #아래
    if x< rows -1:
        if board[x+1][y]<max_virus:
            board[x+1][y]+=1
        else :
            check(x+1,y,board,max_virus,rows,columns)
    #왼쪽
    if y>0 :
        if board[x][y-1]<max_virus:
            board[x][y-1]+=1
        else : 
            check(x,y-1,board,max_virus,rows,columns)
    #오른쪽
    if y<columns-1:
        if board[x][y+1]<max_virus:
            board[x][y+1]+=1
        else : 
            check(x,y+1,board,max_virus,rows,columns)

def solution(rows, columns, max_virus, queries):
    board = [[0]*columns for _ in range(rows)]

    for i in range(len(queries)):
      queries[i][0]-=1
      queries[i][1]-=1
    
    for x,y in queries:
        if board[x][y] < max_virus:
            board[x][y]+=1
        else :
            check(x,y,board,max_virus,rows,columns)
           
    return board

solution(3,4,2,[[3,2],[3,2],[2,2],[3,2],[1,4],[3,2],[2,3],[3,1]])
