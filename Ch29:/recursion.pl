factorial(1,1).
factorial(N,F):-
	M is N-1,
	factorial(M,X),
	F is N*X.

bunnyEars(0,0).
bunnyEars(N,F):-		
	M is N-1,
	bunnyEars(M,X),
	F is X+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,F):-
	M is N-1,
	Q is N-2,
	fibonacci(M,X),
	fibonacci(Q,Y),
	F is X+Y.

ears2(0,0).
ears2(N,F):-
	M is N-1,
	ears2(M,X),
	Y is M mod2,
	F is M+2+X.
	
triangle(0,0).
triangle(1,1).
triangle(N,F):-
	X is N-1,
	triangle(Y,T),
	F is T+N.

sumdigit(0,0).
sumdigit(N,F):-
	X is N//10,
	sumdigit(X,Y),
	F is N+Y mod 10.
	
count7(0,0).
count7(N,F):-
	X is N//10,
	B is N mod 10,
	count7(N,Y),
	F is Y+B//7-B//8.