% Facts and rules about trust and connection
agent(luna).
agent(milo).
agent(nova).

trusts(luna, milo).
trusts(milo, nova).

connected(X, Y) :- trusts(X, Y).
connected(X, Y) :- trusts(Y, X).

verify(Query) :- call(Query), write('true'), nl.
verify(_) :- write('false'), nl.
