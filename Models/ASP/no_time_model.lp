%%%%% INSTANCE %%%%%
%stone facts have format stone((N1, N2), ID) where N1 and N2 are the two numbers on the stone and ID is the stone's unique identifier (supposed to be incremental, starting at 1)
%board size constant is named n
%%%%% RULES %%%%%
%basic facts
size(n).
coordinates(1..n,1..n).
stone_number(N) :- stone((N, _), _).
stone_number(N) :- stone((_, N), _).
stone_id(ID) :- stone(_, ID).
stone_opposite(B, (A, ID)) :- stone((A, B), ID).
stone_opposite(A, (B, ID)) :- stone((A, B), ID).
%last(T) :- time(T), not T = n
%placement coordinates = 0 means no placement
1 { placed_stone((0..n, 0..n), (A, ID)); placed_stone((0..n, 0..n), (B, ID)) } 1 :- stone((A, B), ID).
1 { stone_tail((0..n, 0..n), (A, ID)); stone_tail((0..n, 0..n), (B, ID)) } 1 :- stone((A, B), ID).
%stone placements must be adjacent to their tail
stone_tail((X+1, Y), (B, ID)), stone_tail((X-1, Y), (B, ID)), stone_tail((X, Y+1), (B, ID)), stone_tail((X, Y-1), (B, ID)) :- placed_stone((X, Y), (A, ID)), stone_opposite(B, (A, ID)).
%stone tails may be followed by an adjecent placement
placed_stone((X+1, Y), (A, ID)), placed_stone((X-1, Y), (A, ID)), placed_stone((X, Y+1), (A, ID)), placed_stone((X, Y-1), (A, ID)) :- stone_tail((X, Y), (A, ID1)), stone_id(ID).
%stone tails cannot overlap with placements nor can anything get out of bounds
:- stone_tail((X, Y), _), placed_stone((X, Y), _).
:- stone_tail((X, _), _), not X=0..n.
:- stone_tail((_, Y), _), not Y=0..n.
:- placed_stone((X, _), _), not X=0..n.
:- placed_stone((_, Y), _), not Y=0..n.

%%%% EASY RENDERING %%%%
placement(X, Y, 1, N, ID) :- placed_stone((X, Y), (N, ID)), coordinates(X, Y).
placement(X, Y, 1, N, ID) :- stone_tail((X, Y), (N, ID)), coordinates(X, Y).

%%%% OPTIMIZATION %%%%
%#minimize {1: placement(_, _, 0, _, _)}.
%:~ placed_stone(0, _). [1@1]
:~ placed_stone((0, _), _). [1@1]
:~ placed_stone((_, 0), _). [1@1]
#show placement/5.