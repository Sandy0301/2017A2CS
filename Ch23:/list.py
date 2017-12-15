#Sandy S3C3 list
NullPointer=-1
class node:
    def init(self):
        self.Data=''
        self.Pointer=NullPointer
        
def List():
    SP=NullPointer 
    FLP=0 
    List=[node()for i in range (8)]
    for i in range (7):
        List[i].Pointer=i+1
    List[7].Pointer=NullPointer
    return(List,SP,FLP)

def InsertNode(List,SP,FLP,NI):
    if FLP!=NullPointer:
        NNP=FLP
        List[NNP].Data=NI
        FLP=List[FLP].Pointer
        PNP=NullPointer
        TNP=SP
        while TNP!=NullPointer and List[TNP].Data<NI:
            PNP=TNP
            TNP=List[TNP].Pointer
        if PNP==NullPointer:
            List[NNP].Pointer=SP
            SP=NNP
        else:
            List[NNP].Pointer=List[PNP].Pointer
            List[PNP].Pointer=NNP
    return(List,SP,FLP)

def FindNode(List,SP,DI):
    NNP=SP
    while NNP!=NullPointer and List[NNP].Data!=DI:
        NNP=List[NNP].Pointer

def Delete(List,SP,FLP,DI):
    TNP=SP
    while TNP!=NullPointer and List[TNP].Data!=DI:
        PNP=TNP
        TNP=List[TNP].Pointer
    if TNP!=NullPointer:
        print('No data')
    else:
        if TNP==SP:
            SP=List[SP].Pointer
        else:
            List[PNP].Pointer=List[TNP].Pointer
        List[TNP].Pointer=FLP
        FLP=TNP
    return (List,SP,FLP)

def output(List,SP):
    CNP=SP
    if SP==NullPointer:
        print('No data on stack')
    while CNP !=NullPointer:
        print(List[CNP].Data)
        CNP=List[CNP].Pointer

List,SP,FLP=List()
NI=22
List,SP,FLP=InsertNode(List,SP,FLP,NI)
NI=12
List,SP,FLP=InsertNode(List,SP,FLP,NI)
NI=30
List,SP,FLP=InsertNode(List,SP,FLP,NI)
NI=7
List,SP,FLP=InsertNode(List,SP,FLP,NI)
NI=10
List,SP,FLP=InsertNode(List,SP,FLP,NI)
NI=58
List,SP,FLP=InsertNode(List,SP,FLP,NI)
output(List,SP)
print('')
DI=30
List,SP,FLP=Delete(List,SP,FLP,DI)
output(List,SP)
print('')
DI=29
List,SP,FLP=Delete(List,SP,FLP,DI)
output(List,SP)
print('')
DI=7
FindNode(List,SP,DI)
DI=23
FindNode(List,SP,DI)



