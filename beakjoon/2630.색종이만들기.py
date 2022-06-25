import sys


white=0
blue=0

def divide_and_conquer(paper,n):
  global white
  global blue
  check=0
  
  for i in range(n):
    check+=sum(paper[i])
  if check==0:
    white+=1
  elif check==n*n:
    blue+=1
  else:
    tmp=[paper[i][0:n//2] for i in range(0,n//2)]
    divide_and_conquer(tmp,n//2)
  
    tmp=[paper[i][n//2:n] for i in range(0,n//2)]
    divide_and_conquer(tmp,n//2)
   

    tmp=[paper[i][0:n//2] for i in range(n//2,n)]
    divide_and_conquer(tmp,n//2)
    

    tmp=[paper[i][n//2:n] for i in range(n//2,n)]
    divide_and_conquer(tmp,n//2)
 




n=int(sys.stdin.readline().rstrip())
paper=[]
for _ in range(n):
  paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

divide_and_conquer(paper,n)

print(white)
print(blue)