import sys


def binary_search(array,target,start,end):
  if start>end:
    return False
  mid=(start+end)//2
  if array[mid]==target:
    return True
  elif array[mid]>target:
    return binary_search(array,target,start,mid-1)
  else:
    return binary_search(array,target,mid+1,end)

n=int(sys.stdin.readline().rstrip())
num_list=[]
for num in list(map(int,sys.stdin.readline().rstrip().split())):
  num_list.append(num)

num_list.sort()
m=int(sys.stdin.readline().rstrip())
for target in list(map(int, sys.stdin.readline().rstrip().split())):
  print(1 if binary_search(num_list,target,0,n-1) else 0)
    

