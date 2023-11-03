%%%%% INSTANCE %%%%%
%stone facts have format stone((N1, N2), ID) where N1 and N2 are the two numbers on the stone and ID is the stone's unique identifier (supposed to be incremental, starting at 1)
%board size constant is named n
%%%%% RULES %%%%%
%basic facts
size(n).
time(1..(n**2)).
coordinates(1..n,1..n).
stone_number(N) :- stone((N, _), _).
stone_number(N) :- stone((_, N), _).
stone_id(ID) :- stone(_, ID).
%last(T) :- time(T), not T = n
%placement time = 0 means no placement
1 { placement(1..n, 1..n, 0..(n**2), A, ID) } 1 :- stone((A, _), ID).
1 { placement(1..n, 1..n, 0..(n**2), B, ID) } 1 :- stone((_, B), ID).
%each cell has up to one placement
3 { T = T1; A = A1; ID = ID1 } 3 :- coordinates(X, Y), placement(X, Y, T, A, ID), placement(X, Y, T1, A1, ID1), stone((A, _), ID), time(T).
%time-adjacent placements also need to be space-adjecent
1 {X1 = X + 1; X1 = X - 1; Y1 = Y + 1; Y1 = Y - 1} 1 :- placement(X, Y, T, _, _), placement(X1, Y1, T + 1, _, _), coordinates(X, Y), coordinates(X1, Y1), time(T).
%placements at even time are followed by the reverse of their stone
placement(X, Y, T+1, B, ID) :- placement(_, _, T, A, ID), T \ 2 = 0, stone((A, B), ID), coordinates(X, Y), time(T).
placement(X, Y, T+1, B, ID) :- placement(_, _, T, A, ID), T \ 2 = 0, stone((B, A), ID), coordinates(X, Y), time(T).
%placements at odd time are followed by a matching number
A = A1 :- placement(_, _, T, A, _), placement(_, _, T+1, A1, _), T \ 2 = 1, stone_number(A), stone_number(A1), time(T).
%each stone is only placed once
1 { X = X1; Y = Y1; T = T1 } 1 :- placement(X, Y, T, _, ID), placement(X1, Y1, T1, _, ID), time(T), coordinates(X, Y), coordinates(X1, Y1), stone_id(ID), T \ 2 = 0.
%there is at most one placement per time step
%:- placement(X, _, T, _, _), placement(X1, _, T, _, _), not X = X1, time(T).
%:- placement(X, Y, T, _, _), placement(X, Y1, T, _, _), not Y = Y1, time(T), X=1..n.
%:- placement(X, Y, T, N, _), placement(X, Y, T, N1, _), not N = N1, time(T).
%:- placement(X, Y, T, N, ID), placement(X, Y, T, N, ID1), not ID = ID1, time(T).
%:- placement(X, Y, T, N, ID), placement(X1, Y1, T, N1, ID1), time(T), not (X, Y, N, ID) = (X1, Y1, N1, ID1), coordinates(X, Y), coordinates(X1, Y1), stone_number(N), stone_number(N1), stone_id(ID), stone_id(ID1).
%:- placement(X, _, T, _, _), placement(X1, _, T, _, _), not X = X1, time(T).
%:- placement(_, Y, T, _, _), placement(_, Y1, T, _, _), not Y = Y1, time(T).
%:- placement(_, _, T, N, _), placement(_, _, T, N1, _), not N = N1, time(T).
%:- placement(_, _, T, _, ID), placement(_, _, T, _, ID1), not ID = ID1, time(T).
%0 { placement(X, Y, T, N, ID) : coordinates(X, Y), stone_number(N), stone_id(ID) } 1 :- time(T).
%4 { X = X1; Y = Y1; N = N1; ID = ID1} 4 :- placement(X, Y, T, N, ID), placement(X1, Y1, T, N1, ID1), coordinates(X, Y), coordinates(X1, Y1), stone_number(N), stone_number(N1), stone_id(ID), stone_id(ID1), time(T).

%%%% OPTIMIZATION %%%%
%#minimize {1: placement(_, _, 0, _, _)}.
:~ placement(_, _, 0, _, _). [1@1]
#show placement/5.