from os import rename
import sys

def check(board,start, end):
  element=board[start][start]
  count=0
  for i in range(start,end):
    for j in range(start,end):
      if board[i][j] != element:
        for a in range(0,end//3):
          for b in range(0,end//3):
            count+=check(board,3*a,3*b)
  count+=1
  return count

n=int(sys.stdin.readline().rstrip())
board=[]

for _ in range(n):
  board.append(list(map(str,sys.stdin.readline().rstrip().split())))

print(check(board,0,n))

