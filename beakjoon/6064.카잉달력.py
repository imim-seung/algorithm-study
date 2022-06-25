import math
import sys


test_case=int(sys.stdin.readline().rstrip())

for _ in range(test_case):

  M,N,x,y=map(int,sys.stdin.readline().rstrip().split())
  if M==N:
    if x==y:
      print(x)
      vaild=True
    else:
      vaild=False
  elif M==x and N==y:
    print(M*N)
    vaild=True
  else : 
    end=(M*N)//math.gcd(N,M) 
    k_list=[x]
    vaild=False

    while x<end:
      x+=M
      k_list.append(x)

    for k in k_list:
      if k%N==y :
        print(k)
        vaild=True
        break

  
  
  if not vaild:
    print(-1)
      

      
  



