male(ali).
male(umer).
male(haider).
female(alia).
female(mirab).

% ageBelowEighteen.
% teen :- ageBelowEighteen.

married(ali, alia).
married(alia, ali).

old(haider).
adult(ali).
adult(alia).
child(umer).
child(mirab).
% child(X):- female(X);male(X), teen.

man(X):- 
	male(X), adult(X).
woman(X):- 
	female(X), adult(X).

oldMan(X):- male(X),old(X).
oldWoman(X):- female(X),old(X) .

boy(X):- 
	male(X), child(X).
girl(X):- 
	female(X), child(X).

husband(X,Y):- 
	man(X), woman(Y), married(X,Y).
wife(X,Y):- 
	woman(X), man(Y), married(X,Y).

father(X,Y):- 
	man(X),child(Y).	
father(X,Y):- 
	oldMan(X),adult(Y).	

mother(X,Y):-
	woman(X),child(Y).
mother(X,Y):-
	oldWoman(X),adult(X).

grandFather(X,Y):- 
	(father(X,Z),father(Z,Y)),oldMan(X),child(Y).
grandMother(X,Y):- 
	(mother(X,Z),mother(Z,Y)),oldWoman(X),child(Y).
	
daughter(X,Y):-
	child(X), female(X), (father(Y,X); mother(Y,X)). 
son(X,Y):-
	(child(X);adult(X)), male(X), (father(Y,X); mother(Y,X)).

brother(X,Y):-
	child(X),child(Y),male(X),(male(Y);female(Y)),
	father(Z,X),father(Z,Y).
sister(X,Y):-
	child(X),child(Y),female(X),(male(Y);female(Y)),
	father(Z,X),father(Z,Y).

