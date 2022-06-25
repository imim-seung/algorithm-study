import sys


def make_q_tree(board,n):
  global quad_tree
  check=0
  for i in range(n):
    check+=sum(board[i])
  if check==0:
    quad_tree+='0'
  elif check==n*n:
    quad_tree+='1'
  else :
    
    quad_tree+='('
    tmp=[board[i][0:n//2] for i in range(0,n//2)]
    make_q_tree(tmp,n//2)
    tmp=[board[i][n//2:] for i in range(0,n//2)]
    make_q_tree(tmp,n//2)
    tmp=[board[i][0:n//2] for i in range(n//2,n)]
    make_q_tree(tmp,n//2)
    tmp=[board[i][n//2:] for i in range(n//2,n)]
    make_q_tree(tmp,n//2)
    quad_tree+=')'
    

n=int(sys.stdin.readline().rstrip())
board=[]

for _ in range(n):
  board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

quad_tree=''

make_q_tree(board,n)
print(quad_tree)




