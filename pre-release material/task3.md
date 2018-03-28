## task3
3.1
character(habib).
character_type(habib,explorer).
has_skill(habib,timeTravel).
animal(habib,fish).
3.2
CharaterRule(A,B):-
>>character(A),
>animal(B).

3.3
character(maggie).
character(peter).
animal(parrot).
animal(tiger).
skill(dance).
skill(climb).
pet(maggie,parrot).
pet(peter,tiger)
3.4
X=princess.
X=jim.
X=invisibility.
X=jim.
3.5
pet(jim,X).

has_skill(X,fly).

skill(X).

find(A,B):-
>>character_type(C,A),
>pet(C,B).

find(X,princess).