parent(ali,ahmad).
parent(ali,fatema).
parent(ahmad,salem).
parent(fatema,osama).
male(osama).
male(ahmad).
male(ali).
male(salem).
female(fatema).
father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
sibling(X,Y):-parent(Z,Y),parent(Z,Y),X\==Y.
uncle(X,Y):-parent(Z,Y),parent(G,Z),parent(G,Z),X\==Z.
son(X,Y):-parent(Y,X),male(Y).
daughter(X,Y):-parent(Y,X),female(Y).
grandfather(X,Y):-parent(X,Z),parent(Z,Y),male(X).
grandmother(X,Y):-parent(X,Z),parent(Z,Y),female(X).
cousin(X,Y):-sibling(Z,G),parent(Z,X),parent(G,Y),X\==Y,Z\==G.


