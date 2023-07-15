count([],0).
count([H|Y],Z):-count(Y,Z1),
Z is Z1+1.

sum([],Z).
sum([H|T],Z):-sum(T,Z1),
    Z is Z1+H.


add(X,T,[X|T]).

check(X):-X>0 .



