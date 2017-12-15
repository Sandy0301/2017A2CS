#Sandy binary tree
np=-1
class node:
    def initial(self):
        self.left=np
        self.right=np

def tree():
    tree = [node() for i in range(8)]
    rp=np
    fp=0
    for i in range (7):
        tree[i].left=i+1
    tree[7].left=np
    return(tree,rp,fp)

def Insert(tree,rp,fp,ni):
    if fp!=np:
        new=fp
        tree[new].data=ni
        fp=tree[fp].left
        tree[new].left=np
        tree[new].right=np
        if rp==np:
            rp=new
        else:
            tnp=rp
            while tnp!=np:
                pnp=tnp
                if tree[tnp].data>ni:
                    turnleft=True
                    tnp=tree[tnp].left
                else:
                    turnleft=False
                    tnp=tree[tnp].right
            if turnleft==True:
                tree[pnp].left=new
            else:
                tree[pnp].right=new     
    else:
       print('there is no more space for data') 
    return (tree,rp,fp)

def find(tree,rp,si):
    a=rp
    while a!=np and tree[a].data!=si:
        if tree[a].data>si:
            a=tree[a].left
        else:
            a=tree[a].right
    return (a)

def output(tree,rp):
    l=rp
    r=tree[rp].right
    if rp==np:
        print('there is no data')
    while r!=np:
        print(tree[r].data)
        r=tree[r].right
    while l!=np:
        print(tree[l].data)
        l=tree[l].left

tree,rp,fp=tree()
ni=34
tree,rp,fp=Insert(tree,rp,fp,ni)
ni=12
tree,rp,fp=Insert(tree,rp,fp,ni)
ni=56
tree,rp,fp=Insert(tree,rp,fp,ni)
ni=95
tree,rp,fp=Insert(tree,rp,fp,ni)
output(tree,rp)
print('')
si=34
find(tree,rp,si)
