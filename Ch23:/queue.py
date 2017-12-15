#Sandy queue
np=-1
class node:
    def initial(self):
        self.data=''
        self.pointer=''

def stack():
    stack=[node()for i in range(8)]
    sp=np
    flp=0
    for i in range(7):
        stack[i].pointer=i+1
    stack[7].pointer=np
    return(stack,sp,flp)

def push(stack,sp,flp,ni):
    if flp!=np:
        nnp=flp
        stack[nnp].data=ni
        flp=stack[flp].pointer
        stack[nnp].pointer = sp
    else:
        print("there is no space for more data")
    new=flp
    flp=stack[flp].pointer
    stack[new].data=ni
    stack[new].pointer=sp
    sp=new
    return(stack,sp,flp)     

def pop(stack,sp,flp):
    v=sp
    if stack[sp].pointer==np:
        stack[sp].pointer=flp
        sp=np
        flp=sp
    
    else:
        while v!=np:
            if stack[v].pointer==np:
                a=v
            v=stack[v].pointer
        v2=sp
        while v2!=np:
            if stack[v2].pointer==a:
                b=v2
            v2=stack[v2].pointer
        stack[a].pointer=flp
        flp=a
        stack[b].pointer=np
    return(stack,sp,flp)
    if sp == np :
        print("there is no data on stack")
        value = ""
    else :
        ni = stack[sp].data
        tnp = sp
        sp = stack[sp].pointer
        stack[tnp].pointer = flp
        flp = tnp

def output(stack,sp):
    v=sp
    if v==np:
        print('there is no data on stack')
    while v!=np:
        print(stack[v].data)
        v=stack[v].pointer

stack,sp,flp=stack()

ni=32
stack,sp,flp=push(stack,sp,flp,ni)
output(stack,sp)

ni=17
stack,sp,flp=push(stack,sp,flp,ni)
output(stack,sp)
print('')

ni=12
stack,sp,flp=push(stack,sp,flp,ni)
output(stack,sp)
print('')

ni=40
stack,sp,flp=push(stack,sp,flp,ni)
output(stack,sp)
print('')

stack,sp,flp=pop(stack,sp,flp)
output(stack,sp)
print('')
stack,sp,flp=pop(stack,sp,flp)
output(stack,sp)
print('')
stack,sp,flp=pop(stack,sp,flp)
output(stack,sp)
print('')
stack,sp,flp=pop(stack,sp,flp)
output(stack,sp)
print('')



