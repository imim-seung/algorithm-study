import sys

test_case=int(sys.stdin.readline().rstrip())

add_123=[0]*11
for _ in range(test_case):
  n=int(sys.stdin.readline().rstrip())
  for i in range(1,n+1):
    if i==1 or i==2:
      add_123[i]=i
    elif i==3:
      add_123[i]=4
    else:
      add_123[i]=add_123[i-1]+add_123[i-2]+add_123[i-3]

  print(add_123[n])

  