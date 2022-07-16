import sys

n=int(sys.stdin.readline().rstrip())
house_list=[]
dp=[[0]*3 for _ in range(n)]

for _ in range(n):
  house_list.append(list(map(int,sys.stdin.readline().rstrip().split())))
  
dp[0][0],dp[0][1],dp[1][2]=house_list[0][0],house_list[0][1],house_list[0][2]

for i in range(n):
  dp[i][0]=min(dp[i-1][1]+house_list[i][0],dp[i-1][2]+house_list[i][0])
  dp[i][1]=min(dp[i-1][0]+house_list[i][1],dp[i-1][2]+house_list[i][1])
  dp[i][2]=min(dp[i-1][0]+house_list[i][2],dp[i-1][1]+house_list[i][2])

print(min(dp[n-1][0],dp[n-1][1],dp[n-1][2]))




  


