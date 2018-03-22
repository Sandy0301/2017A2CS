ancestor(A,B):-
	parent(A,B).
ancestor(A,B):-
	parent(A,X),
	ancestor(X,B).