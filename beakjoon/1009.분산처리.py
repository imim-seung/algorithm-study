import sys

test_case=int(sys.stdin.readline().rstrip())
num_dic={
    1:[1,1,1,1],
    2:[2,4,8,6],
    3:[3,9,7,1],
    4:[4,6,4,6],
    5:[5,5,5,5],
    6:[6,6,6,6],
    7:[7,9,3,1],
    8:[8,4,2,6],
    9:[9,1,9,1],
    0:[10,10,10,10]
  }


for _ in range(test_case):
  last_list=[]
  a,b= map(int,sys.stdin.readline().rstrip().split())
  a=a%10
  last_list=num_dic[a]
  print(last_list[b%4])
  