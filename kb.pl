fact(item1).
fact(item2).
related(item1, item2).

rule_example(X, Y) :- related(X, Y).

respond(Query) :- call(Query), write('true'), nl.
respond(_) :- write('false'), nl.
