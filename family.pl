male(de).
male(yuan).
male(shu).
male(zong).

female(fei).
female(yi).
female(julie).

parent(julie,yi).
parent(de,yuan).
parent(shu,de).
parent(zong,shu).
parent(julie,fei).
parent(de,yi).

issister(X,Y) :- 
	parent(S,Y),
	parent(S,X), 
	female(X),
	female(Y),
	not(X=Y).

isbrother(X,Y):-
	parent(S,X),
	parent(S,Y),
	male(X),
	male(Y),
	not(X=Y).

isdaughter(X,Y):-
	parent(Y,X),
	female(X).

isson(X,Y):-
	parent(Y,X),
	male(X).

ismarried(X,Y):-
	parent(X,C),
	parent(Y,C).

isancestor(X,Y):-
	parent(X,C),
	parent(C,D),
	parent(D,Y).
	not(X=Y).
