import sys

n=int(sys.stdin.readline().rstrip())

num_list=[0]*21



for _ in range(n):
  command=sys.stdin.readline().rstrip()
  if not command[-1].isdigit():
    if command =='all':
      num_list=[1]*21

    else:
      num_list=[0]*21



  else:
    c,num=command.split()
    num=int(num)
    if c=='add':
      num_list[num]=1
    elif c =='check':
      print(num_list[num])
    elif c=='remove':
      num_list[num]=0
    else:
      if num_list[num]==0:
        num_list[num]=1
      else:
        num_list[num]=0
    


    


