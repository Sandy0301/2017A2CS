parent(jean,jack).
parent(fred,paul).
parent(ann,alia).

ancestor(A,B):-
	parent(A,B).
ancestor(A,B):-
	parent(A,X),
	ancestor(X,B).