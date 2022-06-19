import sys 

n=int(sys.stdin.readline().rstrip())
squares=[0]*224
dp=[0]*(n+1)
dp[0]=0
dp[1]=1

for i in range(2,n+1,1):
  

  dp[i]=1+dp[i-(j**2)]


print(dp[n])





