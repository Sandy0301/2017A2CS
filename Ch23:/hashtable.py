#Sandy option1 this is my hash table

hashtable=[("-")for i in range(10)]
def hash(key):
    adr=key%10
    return(adr)

def insert(key):
    adr=hash(key)
    while hashtable[adr]!='-':
        adr=adr+1
        if adr>9:
            adr=0
    print(adr,key)
    hashtable[adr]=key

def find(sk):
    i=1
    adr=hash(sk)
    while (hashtable[adr]!=sk)and (hashtable[adr]!='-') and (i==len(hashtable)) :
        adr=adr+1
        if adr>9:
            adr=0
        i=i+1
    if  hashtable[adr]!='-':
        print('')
        print(adr,hashtable[adr])


key=25
key=insert(key)
key=26
key=insert(key)
key=1
key=insert(key)
key=97
key=insert(key)
key=43
key=insert(key)
key=85
key=insert(key)

sk=36
find(sk)
print(hashtable)
