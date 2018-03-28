#This is the solution for the end of chapter25 questions.
#Sandy

1.a iteration is repeated process of running code within a function. Recursion calls itself using corresponding local variables.
b. the advantage is that it proceeds fast since it has shorter procedures compared with iteration.

2.a. it is a recursion with given local variables.
b. 
|call number|procedure call|exponent=1|result
| 1         |power(2,4)    |False     |
| 2         |power(2,3)    |False     |
| 3         |power(2,2)    |False     |
| 4         |power(2,1)    |False     |
| 5         |power(2,0)    |True      |1
|(4)        |power(2,1)    |          |2*1
|(3)        |power(2,2)    |          |2*2
|(2)        |power(2,3)    |          |2*3
|(1)        |power(2,4)    |          |2*4

The result is 16
c.Variables are called to store in the stack. The data are arranged in the order that the last that comes in is the first one to go out.
e.
```Pseudocode
Function power(base,exponent)
	result<-1
	WHILE exponent>0
		result<-result*base
		exponent<-exponent-1
	ENDWHILE
	RETURN result
ENDFUNCTION

f.i.the code makes more sense when debugging
ii.neat code makes it clearer
3.a.i. 04
ii. 06
b.
|call number|procedure call| n=0 | n=1 |result
| 1         |Fibonacci(4)  |False|False|
| 2         |Fibonacci(3)  |False|False|
| 3         |Fibonacci(2)  |False|False|
| 4         |Fibonacci(1)  |False|True |1
| 5         |Fibonacci(0)  |True |False|1
|(3)        |Fibonacci(2)  |     |     |1
|6          |Fibonacci(1)  |False|True |1
|(2)        |Fibonacci(3)  |     |     |3
|7          |Fibonacci(2)  |False|False|
|8          |Fibonacci(1)  |False|True |1
|9          |Fibonacci(0)  |True |False|0
|(7)        |Fibonacci(2)  |     |     |1
|(1)        |Fibonacci(4)  |     |     |3
It will return 3 in the end.