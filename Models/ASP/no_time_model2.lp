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
stone_half(N, ID) :-  stone((N, _), ID).
stone_half(N, ID) :-  stone((_, N), ID).

%Each stone half is followed by at most one more stone half
0 { follows((N1, ID1), (N2, ID2)) : stone_half(N1, ID1) } 1 :- stone_half(N2, ID2).
%There is at least one placement
1 { follows((N1, ID1), (N2, ID2)) : stone_half(N1, ID1), stone_half(N2, ID2)}.
%Only stones can be part of a follow
:- follows((ID, N), (_, _)), not stone_half(ID, N).
:- follows((_, _), (ID, N)), not stone_half(ID, N).
%Same-stone follow pairs are folloed by a different but matching stone. Either that or the sequence ended
follows((N1, ID2), (N1, ID1)), last_stone(N1, ID1) :- follows((N1, ID1), (N2, ID1)), stone_half(N1, ID2).
%Different-stone follow pairs are followed by a same-stone follow pair
follows((N2, ID1), (N1, ID1)) :- follows((N1, ID1), (_, ID2)), stone_opposite(N2, (N1, ID1)).

%%%% EASY RENDERING %%%%
placement(1, 1, 1, N, ID) :- follows((N, ID), (_, _)).
placement(1, 1, 1, N, ID) :- follows((_, _), (N, ID)).

%%%% OPTIMIZATION %%%%
%#minimize {1: placement(_, _, 0, _, _)}.
%:~ placed_stone(0, _). [1@1]
:~ follows((_, _), (_, _)). [-1@1]
#show placement/5.