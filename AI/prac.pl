fac(0,1).
fac(N,X):-N>0,N1 is N-1,
fac(N1,X1),
X is X1*N.

sum(0,0).
sum(N,X):- N1 is N-1,
    sum(N1,X1),
    X is X1+N.


pow(X,0,1).
pow(X,N,Y):-N1 is N-1,
    pow(X,N1,Y1),
    Y is  X*Y1.

size([],0).
size([H|T],X):-size(T,X1),
    X is X1+1

suml([],0).
suml([X|T],S):- suml(T,S1),
    S is S1+X.
find(

