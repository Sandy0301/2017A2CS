#Sandy option1 Dictionary

class node:
    def __init__(h):
        h.key=''
        h.value=''

hashtable=[(node())for i in range(20)]

def hash(key):
    adr=ord(key[0])-97
    return(adr)

def insert(key,value):
    adr=hash(key)
    while hashtable[adr].key!='':
        adr=adr+1
        if adr>19:
            adr=0
    print(adr)
    hashtable[adr].key=key
    hashtable[adr].value=value

def find(sk):
    i=1
    adr=hash(sk)
    while (hashtable[adr].key!=sk)and (hashtable[adr]!='-') and (i==len(hashtable)) :
        adr=adr+1
        if adr>19:
            adr=0
        i=i+1
    if hashtable[adr].key!='':
        print(adr,hashtable[adr].key,hashtable[adr].value)

def output():
    for i in range(len(hashtable)):
        if hashtable[i].key!='':
            print('')
            print(hashtable[i].key,'means',hashtable[i].value)

key='router'
value='a device that acts a node on the internet'
insert(key,value)

key='algorithm'
value='a sequence of steps that can be carried out to perform a task'
insert(key,value)

key='attribute'
value='a column in a relation that contains values'
insert(key,value)
output()
key='router'
find(key)
