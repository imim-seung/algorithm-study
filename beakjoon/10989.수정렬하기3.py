import sys

num=int(sys.stdin.readline().rstrip())

num_list=[0]*10001
for _ in range(num):
  num_list[int(sys.stdin.readline().rstrip())]+=1


for index,n in enumerate(num_list):
  if n > 0:
    for _ in range(n):
      print(index)