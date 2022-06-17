import sys
test_case=int(sys.stdin.readline().rstrip())
p=[0]*101
for _ in range(test_case):
  n=int(sys.stdin.readline().rstrip())
  for i in range(1,n+1):
    if i<4:
      p[i]=1
    elif i<6:
      p[i]=2
    else:
      p[i]=p[i-1]+p[i-5]

  print(p[n])
