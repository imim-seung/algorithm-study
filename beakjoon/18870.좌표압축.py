import sys

n=sys.stdin.readline().rstrip()
num_list=[]
for i , n in enumerate(list(map(int,sys.stdin.readline().rstrip().split()))):
  num_list.append((n,i))

num_list=sorted(num_list,key=lambda x : x[0])

new_location=0
num=num_list[0][0]
compression=[]
for n in num_list:
  if n[0]!=num:
    new_location+=1
  compression.append((new_location,n[1]))
  num=n[0]

compression.sort(key=lambda x : (x[1],x[0]))

for n in compression:
  print(n[0],end=' ')


    






