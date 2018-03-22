male(fred).
female(alia).
parent(fred,alia).

father(A,B):-
	male(A),
	parent(A,B).