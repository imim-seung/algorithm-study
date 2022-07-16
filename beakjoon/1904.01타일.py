import sys

n=int(sys.stdin.readline().rstrip())

dp=[0]*(n+1)
if n<2:
  print(n)
  sys.exit()

dp[1],dp[2]=1,2
for i in range(3,n+1):
  dp[i]=(dp[i-1]+dp[i-2])%15746

print(dp[n])