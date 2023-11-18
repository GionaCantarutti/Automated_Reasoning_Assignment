%%%%% INSTANCE %%%%%
%stone facts have format stone((N1, N2), ID) where N1 and N2 are the two numbers on the stone and ID is the stone's unique identifier (supposed to be incremental, starting at 1)
%board size constant is named n
%%%%% RULES %%%%%
%basic facts
size(n).
coordinates(1..n,1..n).
time(1..n**2).
stone_number(N) :- stone((N, _), _).
stone_number(N) :- stone((_, N), _).
stone_id(ID) :- stone(_, ID).
stone_opposite(B, (A, ID)) :- stone((A, B), ID).
stone_opposite(A, (B, ID)) :- stone((A, B), ID).
stone_half(N, ID) :-  stone((N, _), ID).
stone_half(N, ID) :-  stone((_, N), ID).

%%%% PLACEMENTS %%%%
%Each stone half is followed by at most one more stone half
0 { follows((N1, ID1, T+1), (N2, ID2, T)) : stone_half(N1, ID1), time(T) } 1 :- stone_half(N2, ID2).
%There is at least one placement
%1 { follows((N1, ID1), (N2, ID2)) : stone_half(N1, ID1), stone_half(N2, ID2)}.
%The first stone is followed by its other half
follows((N1, ID, 2), (N, ID, 1)) :- placement(1, 1, 1, N, ID), stone_opposite(N1, (N, ID)).
%Only stones can be part of a follow
:- follows((ID, N, _), (_, _, _)), not stone_half(ID, N).
:- follows((_, _, _), (ID, N, _)), not stone_half(ID, N).
%Same-stone follow pairs are folloed by a different but matching stone. Either that or the sequence ended
follows((N1, ID2, T+2), (N1, ID1, T+1)), last_stone(N1, ID1, T) :- follows((N1, ID1, T+1), (N2, ID1, T)), stone_half(N1, ID2), ID1 <> ID2, time(T).
%Different-stone follow pairs are followed by a same-stone follow pair
follows((N2, ID1, T+2), (N1, ID1, T+1)) :- follows((N1, ID1, T+1), (_, ID2, T)), stone_opposite(N2, (N1, ID1)), ID1 <> ID2, time(T).

%%%% TIME/SPACE COORDINATES %%%%
%Time/space coordinates of first placement
placement(1, 1, 1, N, ID) :- follows((_, _, _), (N, ID, 1)), not follows((N, ID, 1), (_, _, _)).
%There is exactly one first placement
1 { placement(1, 1, 1, N, ID) : stone_half(N, ID) } 1.
%Time/space adjacency between following placements
placement(X+1, Y, T+1, N2, ID2), placement(X-1, Y, T+1, N2, ID2), placement(X, Y+1, T+1, N2, ID2), placement(X, Y-1, T+1, N2, ID2) :- follows((N2, ID2, T+1), (N1, ID1, T)), placement(X, Y, T, N1, ID1), coordinates(X, Y), time(T).
%Cannot get out of bounds
:- placement(X, _, _, _, _), X > n.
:- placement(X, _, _, _, _), X < 1.
:- placement(_, Y, _, _, _), Y > n.
:- placement(_, Y, _, _, _), Y < 1.

%%%% OPTIMIZATION %%%%
%#minimize {1: placement(_, _, 0, _, _)}.
%:~ placed_stone(0, _). [1@1]

%:~ follows((_, _), (_, _)). [-1@1]
%Last stone cannot be over n**2 time (could help the solver understanding when it reached the optimum)
:- last_stone(_, _, T), T > n**2.
#maximize {T: last_stone(_, _, T)}.
#show placement/5. 
%#show follows/2.