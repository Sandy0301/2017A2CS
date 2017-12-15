#Sandy S2C3 stack
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
        print("no space for more data")
    value=flp
    flp=stack[flp].pointer
    stack[value].data=ni
    stack[value].pointer=sp
    sp=value
    return(stack,sp,flp)     

def pop(stack,sp,flp):
    flp=sp
    sp=stack[sp].pointer
    return(stack,sp,flp)
    if ap == np :
        print("there is no data on stack")
        value = ""
    else :
        value = stack[sp].data
        tnp = sp
        sp = stack[sp].pointer
        stack[tnp].pointer = flp
        flp = tnp


def output(stack,sp):
    next=sp
    if next==np:
        print('there is no data on stack')
    while next!=np:
        print(stack[next].data)
        next=stack[next].pointer

stack,sp,flp=stack()

value=32
stack,sp,flp=push(stack,sp,flp,value)
output(stack,sp)

value=17
stack,sp,flp=push(stack,sp,flp,value)
output(stack,sp)
print('')

value=12
stack,sp,flp=push(stack,sp,flp,value)
output(stack,sp)
print('')

value=40
stack,sp,flp=push(stack,sp,flp,value)
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
