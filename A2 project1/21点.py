#This is the code for BlackJack
import random

def ask(comment,r1,r2):
    while True:
        r==input(comment)
        if r==r1 or r==r2:
            return r

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
    n=random.randrange(1,13+1)
    display(name,n)
    if n>10:
        return 10
    else:
        return n

def end(n):
    if n>21:
        print('End')
        return -1
    else:
        return n

def continue(n):
    if n<=21:
        option=ask('Do you want to continue or end?','end','continue')
        if option=='end':
            return True
        return False























