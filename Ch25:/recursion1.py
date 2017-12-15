#Sandy Option1
#This is a solutions for recursion1 in codingbat
def factorial (n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

def BunnyEars(bunnies):
    if bunnies==0:
        return 0
    return 2+BunnyEars(bunnies-1)
print(BunnyEars(3))

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return  fibonacci (n-1)+ fibonacci (n-2)
print( fibonacci (4))

def ears2(bunnies):
    if bunnies==0:
        return 0
    if bunnies%2==1:
        return ears2(bunnies-1)+2
    else:
        return ears2(bunnies-1)+3
print(ears2(5))

def triangle(rows):
    if rows==0:
        return 0
    if rows==1:
        return 1
    return rows+triangle(rows-1)
print(triangle(4))

def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
print(sum(123))
        
def count7(n):
    if n==0:
        return 0
    if n%10==7:
        return 1+count7(n//10)
    return count7(n//10)
print (count7(717))

def count8(n):
    if n==0:
        return 0
    if n%10==8:
        return 1+count8(n//10)
        if (n//10)%10==8:
            return 2+count8()
    return count8(n//10)
print(count8(18))

def powerN(base,n):
    if n==0:
        return 1
    return base**n
print (powerN(2,3))

def CountX(str):
    if str == '':
        return 0 
    if str[-1:] == 'x':
        return 1 + CountX(str[:-1])
    else:
        return CountX(str[:-1])
print(CountX('xxxf'))

def CountHi(str):
    if str == '':
        return 0 
    if str[-2:] == 'hi':
        return 1 + CountHi(str[:-1])
    else:
        return CountHi(str[:-1])
print(CountHi('xxhixxh'))    

def ChangeXY(str):
    if str == '':
        return ''
    if str[-1:] == 'x':
        return ChangeXY(str[:-1]) + 'y'
    else:
        return ChangeXY(str[:-1]) + str[-1]
print(ChangeXY('xxfhxy'))    

def ChangePi(str):
    if str == '':
        return ''
    if str[-2:] == 'pi':
        return ChangePi(str[:-2]) + '3.14'
    else:
        return ChangePi(str[:-1]) + str[-1]
print(ChangePi('ipipip'))

def noX(str):
    if str=='':
        return ''
    if str[-1:]=='x':
        return noX(str[:-1])
    return noX(str[:-1])+str[-1]
print(noX('xxxvbdjx'))

def Array6(n,i):
    if i==len(n):
        return False
    if n[i]==6:
        return True
    return Array6(n,i+1)
print(Array6([2,7,4],0))

def Array11(n,i):
    if i==len(n):
        return False
    if n[i]==11:
        return 1+Array11(n,i+1)
    return Array11(n,i+1)
print(Array11([1,2,11,111],0))

def array220(n, i):
    if len(n)==1:
        return False
    if len(n)==2 and (n[i]*10) != n[i+1]:
        return False
    if ((n[i]*10)==n[i+1]) and (i+1<len(n)):
        return True
    return array220(n,i+1)
print(array220([2,3,5,50,81,93],0))

def allstar(str):
    if str=='':
        return ''
    if len(str)==1:
        return str
    return str[0]+'*'+allstar(str[1:])
print(allstar('hello'))

def pairstar(str):
    if str=='':
        return ''
    if len(str)==1:
        return str
    if str[0]==str[1] and len(str)>1:
        return str[0]+'*'+pairstar(str[1:])
    return str[0]+pairstar(str[1:])
print(pairstar('dgnnqjiii'))

def endX(str):
    if str=='':
        return ''
    if str[0]=='x':
        return endX(str[1:])+'x'
    return str[0]+endX(str[1:])
print(endX('ddxghvnxc'))

def countPairs(str):
    if str=='':
        return ''
    if len(str)<=2:
        return 0
    if str[0]==str[2]:
        return 1+countPairs(str[1:])
    return countPairs(str[1:])
print(countPairs('abebdaua'))

def countAbc(str):
    if str=='':
        return 0
    if len(str)>2 and str[0:3]=='abc':
        return 1+countAbc(str[3:])
    if len(str)>2 and str[0:3]=='aba':
        return 1+countAbc(str[1:])
    return countAbc(str[1:])
print(countAbc("abcxababa"))

def count11(str):
    if str=='':
        return 0
    if len(str)>1 and str[0:2]=='11':
        return 1+count11(str[2:])
    return count11(str[1:])
print(count11('sed11nd1111'))

def stringClean(str):
    if str=='':
        return ''
    if len(str)>1 and str[0]==str[1]:
        return stringClean(str[1:])
    return str[0]+stringClean(str[1:])
print(stringClean('abbvcccxz'))

def countHi2(str):
    if str=='':
        return 0
    if str[0:3]=='xhi':
        return 0+countHi2(str[3:])
    if str[0:2]=='hi':
        return 1+countHi2(str[1:])
    return 0+countHi2(str[1:])
print(countHi2('hhihixhiashihi'))

def parenBit(str):
    if str=='':
        return ''
    if len(str)>=2 and str[0]!='(':
        return parenBit(str[1:])
    if len(str)>=2 and str[-1]!=')':
        return parenBit(str[:-1])
    return str
print(parenBit('sfg(f34s)df'))

def nestParen(str):
    if str=='':
        return True
    if str[0]=='(' and str[-1]==')':
        return nestParen(str[1:-1])
    return False
print(nestParen('(())'))

def strCount(str,sub):
    if sub=='' or str=='':
        return 0
    if str[0:len(sub)]==sub:
        return 1+strCount(str[len(sub):],sub)
    return strCount(str[1:],sub)
print(strCount('owapapacatapple','apa'))

def strCopies(str, sub, n):
    if str==''and n==0:
        return True
    if str=='' and n!=0:
        return False
    if str[0:len(sub)]==sub:
        n=n-1
        return strCopies(str[len(sub):], sub, n)
    return strCopies(str[1:], sub, n)
print(strCopies('cowcatdog','cow',8))

def strDist(str, sub):
    if str[0:3] != sub:
        return strDist(str[1:], sub)
    if str[-3:] != sub:
        return strDist(str[:-1], sub)
    return len(str)
print(strDist("catcowcat", 'cat'))
