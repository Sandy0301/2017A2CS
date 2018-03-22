factorial(0,1).
factorial(N,R):-
	M is N-1,
	factorial(M,P),
	R is P*N.