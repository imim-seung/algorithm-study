def start_to_minus(n):
  count=0
  while n !=1:
    n-=1
    count+=1
    if n%3==0:
      n/=3
      count+=1
      continue

    if n % 2 ==0:
      n/=2
      count+=1
      continue
  return count


  
num=int(input())
print(min(start_to_minus(num),start_to_check(num)))

  
