import sys

fibo_call=[[0,0] for _ in range(41)]

test_case=int(sys.stdin.readline().rstrip())
for _ in range(test_case):
  n=int(sys.stdin.readline().rstrip())
  for i in range(0,n+1):
    if i==0:
      fibo_call[i]=[1,0]
    elif i==1:
      fibo_call[i]=[0,1]
    else :
      fibo_call[i][0]=fibo_call[i-1][0]+fibo_call[i-2][0]
      fibo_call[i][1]=fibo_call[i-1][1]+fibo_call[i-2][1]


  print(fibo_call[n][0], end=' ')
  print(fibo_call[n][1])



