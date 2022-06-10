import sys
from collections import defaultdict


n=int(sys.stdin.readline().rstrip())
num_list=[]
for _ in range(n):
  num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()
#산술평균
print(round(sum(num_list)/n))

#중앙값
print(num_list[n//2])

#최빈값
num_dic=defaultdict(int)
frequency=[]
for n in num_list:
  num_dic[n]+=1

max_value=max(num_dic.values())
for num, c in num_dic.items():
  if c==max_value:
    frequency.append(num)

if len(frequency)==1:
  print(frequency[0])
else:
  print(frequency[1])

#범위
print(abs(num_list[-1]-num_list[0]))
