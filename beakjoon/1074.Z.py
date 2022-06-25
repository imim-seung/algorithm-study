import sys
sys.setrecursionlimit(10**6)


def z_visit(size ,x,y,r,c,count):

  if size==2:
    count+=1
    visit = [(x,y), (x,y+1),(x+1,y),(x+1,y+1)]
    for i,v in enumerate(visit):
      if v[0]==r and v[1]==c:
        print(count*4+i)
        return 
  else : 
    count=z_visit(size//2 ,x,y,r,c,count)
    +z_visit(size//2,x,y+(size//2),r,c,count)
    +z_visit(size//2,x+(size//2),y,r,c,count)
    +z_visit(size//2,x+(size//2),y+(size//2),r,c,count)

  return count



n,r,c=map(int,sys.stdin.readline().rstrip().split())

z_visit(2**n,0,0,r,c,0)

