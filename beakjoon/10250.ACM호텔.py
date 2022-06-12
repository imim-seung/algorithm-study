import sys

n=int(sys.stdin.readline().rstrip())
for _ in range(n):
  h,w,guest=map(int,sys.stdin.readline().rstrip().split())
  room=str(guest%h) if guest%h !=0 else str(h) 
  num=(guest//h) if guest%h ==0 else  guest//h +1
  if num <10:
    room+='0'
  print(room+str(num))
