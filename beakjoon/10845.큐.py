import sys


n=int(sys.stdin.readline().rstrip())
q=[]
for _ in range(n):
    command=sys.stdin.readline().rstrip()
    if command.isalpha():
        if command =='pop':
            if q :
                print(q.pop(0))
            else:
                print(-1)
        elif command =='size':
            print(len(q))
        elif command=='empty':
            if q:
                print(0)
            else:
                print(1)
        elif command=='front':
            if q:
                print(q[0])
            else : 
                print(-1)
        else:
            if q:
                print(q[-1])
            else:
                print(-1)

    else:
        c ,element=command.split()
        q.append(int(element))
