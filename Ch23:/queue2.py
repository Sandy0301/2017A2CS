#Sandy queue
np=-1

class Node :
   def __init__(self) :
      self.Data = ""
      self.Pointer = np

def initialise() :
    queue = [Node() for i in range(8)]
    flp=0
    sp=np
    ep=np
    for Index in range(7) :
        queue[Index].Pointer = Index + 1
        queue[7].Pointer =np
    return(queue,sp,ep,flp)

def add(queue,sp,ep,flp,new) :
    if flp!=np :
        nnp=flp
        queue[nnp].Data=new
        flp= queue[flp].Pointer
        queue[nnp].Pointer = np
        if ep == np:
            sp=nnp
        else :
            queue[ep].Pointer=nnp
        ep=nnp
    else :
        print("there is no more space")
    return(queue,sp,ep,flp)

def leave(queue,sp,ep,flp) :
    if sp!=np : 
        Value = queue[sp].Data
        tnp = queue[sp].Pointer
        if tnp==np:
            ep = np
        queue[sp].Pointer = flp
        flp= sp
        sp=tnp
    else :
        print("queue empty")
        Value = ""
    return(queue,sp,ep,flp,Value)

def output(queue,sp) :
    cnp = sp
    if sp == np:
        print("No data in list")
    while cnp!=np :
        print(cnp, " ",queue[cnp].Data)
        cnp= queue[cnp].Pointer

queue,sp,ep,flp=initialise()
ni=32
queue,sp,ep,flp=add(queue,sp,ep,flp,ni)
output(queue,sp)
print('')

ni=10
queue,sp,ep,flp=add(queue,sp,ep,flp,ni)
output(queue,sp)
print('')

ni=34
queue,sp,ep,flp=add(queue,sp,ep,flp,ni)
output(queue,sp)
print('')

ni=2
queue,sp,ep,flp=add(queue,sp,ep,flp,ni)
output(queue,sp)
print('')


queue,sp,ep,flp,Value=leave(queue,sp,ep,flp)
output(queue,sp)
print('')
