import sys

n=int(sys.stdin.readline().rstrip())
restaurant=list(map(int,sys.stdin.readline().rstrip().split()))
people=int(sys.stdin.readline().rstrip())

index=n//people
arr=[]

for i in range(0,n,index):
  arr=restaurant[i:i+index]
  arr.sort()
  for j in arr:
    print(j,end=' ')







