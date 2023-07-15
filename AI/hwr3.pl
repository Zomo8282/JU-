sum(0,0).
sum(X,Y):- X>0,
    X1 is X-1,
    sum(X1,Y1),
    Y is Y1+X.
