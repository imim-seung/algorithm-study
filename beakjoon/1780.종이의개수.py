from struct import pack_into
import sys

sys.setrecursionlimit
def check(x,y,n):
  element=board[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if board[i][j] != element:
        for a in range(3):
          for b in range(3):
            check(x+a*(n//3),y+b*(n//3),n//3)
        return
  if element=='-1':
    paper[0]+=1
  elif element=='0':
    paper[1]+=1
  else :
    paper[2]+=1
  

n=int(sys.stdin.readline().rstrip())
board=[]
paper=[0,0,0]

for _ in range(n):
  board.append(list(map(str,sys.stdin.readline().rstrip().split())))

check(0,0,n)
print(*paper , sep='\n')

