import random

def name():
    name1=input('Enter player 1 username: ')
    name2=input('Enter player 2 username: ')
    return name1, name2

def display(name,n):
    if n==1:
        n='Ace'
    if n==11:
        n='Jack'
    if n==12:
        n='Queen'
    if n==13:
        n='King'
    else:
        n=str(n)
    print(name,'gets a',n)

def process(name):
    n=random.randrange(1,14)
    display(name,n)
    if n>10:
        return 10
    else:
        return n

def thisplayerend(name,total):
    print('')
    print('---------[Player:',name,']---------')
    if total>21:
        return True
    if continueend(name,total)==False:
        return True
    return False

def continueend(name,total):
    print('Total:',total)
    choice=input('Do you want to continue or end?')
    if choice=='end':
        return False
    return True
    
def thisplayerturn(name):
    print('Pass the device to', name)
    total=0
    while thisplayerend(name,total)==False:
        n=process(name)
        total=total+n
    if total>21:
        total=total-1
    return total

def main():
    name1,name2=name()
    score1=thisplayerturn(name1)
    print('')
    score2=thisplayerturn(name2)
    if score1==score2:
        print('Player',name1,'and Player',name2, 'tie!')
    if score1>score2:
        print(name1,'wins')
    if score1<score2:
        print(name2,'wins')

main()
