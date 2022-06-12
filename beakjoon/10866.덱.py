import sys


n=int(sys.stdin.readline().rstrip())
deq=[]
for _ in range(n):
    command=sys.stdin.readline().rstrip()
    if command[-1].isalpha():
        if command =='pop_front':
            if deq :
                print(deq.pop(0))
            else:
                print(-1)
        elif command =='pop_back':
            if deq :
                print(deq.pop())
            else:
                print(-1)
        elif command =='size':
            print(len(deq))
        elif command=='empty':
            if deq:
                print(0)
            else:
                print(1)
        elif command=='front':
            if deq:
                print(deq[0])
            else : 
                print(-1)
        else:
            if deq:
                print(deq[-1])
            else:
                print(-1)

    else:
        c ,element=command.split()
        if c=='push_front':
            deq=[int(element)]+deq

        else:
            deq.append(int(element))
