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
1 { placed_stone(0..(n**2), (A, ID)) } 1 :- stone((A, _), ID).
1 { placed_stone(0..(n**2), (B, ID)) } 1 :- stone((_, B), ID).
%each cell has exactly one placement
1 { position(X, Y, T) : time(T) } 1 :- coordinates(X, Y).
%each time step has up to one position
:- { position(_, _, T) } > 1; time(T).
%at most one stone is placed per time step
:- { placed_stone(T, _) } > 1; time(T).
%time-adjacent placements also need to be space-adjecent
%1 {X1 = X + 1; X1 = X - 1; Y1 = Y + 1; Y1 = Y - 1} 1 :- placement(X, Y, T, _, _), placement(X1, Y1, T + 1, _, _), coordinates(X, Y), coordinates(X1, Y1), time(T).
%placements at even time are followed by the reverse of their stone
%placement(X, Y, T+1, B, ID) :- placement(_, _, T, A, ID), T \ 2 = 0, stone((A, B), ID), coordinates(X, Y), time(T).
%placement(X, Y, T+1, B, ID) :- placement(_, _, T, A, ID), T \ 2 = 0, stone((B, A), ID), coordinates(X, Y), time(T).
%placements at odd time are followed by a matching number
%A = A1 :- placement(_, _, T, A, _), placement(_, _, T+1, A1, _), T \ 2 = 1, stone_number(A), stone_number(A1), time(T).

%%%% EASY RENDERING %%%%
placement(X, Y, T, N, ID) :- placed_stone(T, (N, ID)), position(X, Y, T).

%%%% OPTIMIZATION %%%%
%#minimize {1: placement(_, _, 0, _, _)}.
:~ placed_stone(0, _). [1@1]
#show placement/5.