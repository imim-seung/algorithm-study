import sys 

n=int(sys.stdin.readline().rstrip())
squares=[0]*224
for i in range(1,224):
  squares[i]=i*i

num=[]
copy_n=n
start=round(n**0.5)
while n>0 and len(num)<5:
  for i in range(start,0,-1):
    if squares[i]<=n:
      n-=squares[i]
      num.append(i)
  if len(num)>5:
    start=num[0]-1
    num=[]
    n=copy_n
  if n>0:
    start=round(n**0.5)
  

print(len(num))





