%%%%%%%%%%%%%%%%%%%%
%%%%% INSTANCE %%%%%
%%%%%%%%%%%%%%%%%%%%

%stone facts have format stone((N1, N2), ID) where N1 and N2 are the two numbers on the stone and ID is the stone's unique identifier (supposed to be incremental, starting at 1)
%board size constant is named n
%instance facts are supposed to be automatically added before solving the program

%%%%%%%%%%%%%%%%%
%%%%% RULES %%%%%
%%%%%%%%%%%%%%%%%

%%%%%%%% BASIC HELPER FACTS %%%%%%%%
coordinates(1..n,1..n).
time(1..n**2).
stone_opposite(B, (A, ID)) :- stone((A, B), ID).
stone_opposite(A, (B, ID)) :- stone((A, B), ID).
stone_half(N, ID) :-  stone((N, _), ID).
stone_half(N, ID) :-  stone((_, N), ID).

%%%%%%%%%%%%% FOLLOWS  %%%%%%%%%%%%%
%Each stone half is followed by at most one more stone half
{ follows((N1, ID1, T+1), (N2, ID2, T)) : stone_half(N1, ID1), time(T) } <= 1 :- stone_half(N2, ID2).
%Only the first stone is allowed to not have a predecessor
:- follows((N1, ID1, T+1), (N2, ID2, T)), T > 1, not follows((N2, ID2, T), (_, _, _)).
%There is exactly one final placement
{ follows((-1, -1, T+1), (N, ID, T)) : time(T), stone_half(N, ID) } = 1.
%The first stone is followed by its other half
follows((N1, ID, 2), (N, ID, 1)) :- placement(1, 1, 1, N, ID), stone_opposite(N1, (N, ID)).
%Only stones can be part of a follow (probably unecessary)
:- follows((N, ID, _), (_, _, _)), not stone_half(N, ID), ID <> -1, N <> -1.
:- follows((_, _, _), (N, ID, _)), not stone_half(N, ID).
%Same-stone follow pairs are folloed by a different but matching stone. Either that or the sequence ended. The first missing placement is signaled by a (-1, -1) stone
1 { follows((N1, ID2, T+2), (N1, ID1, T+1)) : stone_half(N1, ID2), ID1 <> ID2, time(T+2) ; follows((-1, -1, T+2), (N1, ID1, T+1)) } 1 :- follows((N1, ID1, T+1), (N2, ID1, T)), time(T).
%Different-stone follow pairs are followed by a same-stone follow pair
follows((N2, ID1, T+2), (N1, ID1, T+1)) :- follows((N1, ID1, T+1), (_, ID2, T)), stone_opposite(N2, (N1, ID1)), ID1 <> ID2, time(T).

%%%%%% TIME/SPACE COORDINATES %%%%%%%
%Time/space coordinates of first placementp
placement(1, 1, 1, N, ID) :- follows((_, _, _), (N, ID, 1)), not follows((N, ID, 1), (_, _, _)).
%There is exactly one first placement
1 { placement(1, 1, 1, N, ID) : stone_half(N, ID) } 1.
%Time/space adjacency between following placements
placement(X+1, Y, T+1, N2, ID2), placement(X-1, Y, T+1, N2, ID2), placement(X, Y+1, T+1, N2, ID2), placement(X, Y-1, T+1, N2, ID2) :- follows((N2, ID2, T+1), (N1, ID1, T)), placement(X, Y, T, N1, ID1), coordinates(X, Y), time(T), stone_half(N1, ID1), stone_half(N2, ID2).
%Cannot get out of bounds
:- placement(X, Y, _, _, _), not coordinates(X, Y).
:- placement(_, _, T, _, _), not time(T).
%Placements cannot overlap
:- placement(X1, Y1, T1, _, _), placement(X2, Y2, T2, _, _), T1 <> T2, X1 = X2, Y1 = Y2.

%%%%%%%%%%%%%%%%%%%%%%
%%%% OPTIMIZATION %%%%
%%%%%%%%%%%%%%%%%%%%%%

#maximize {T: follows((-1, -1, T), (_, _, _))}.
#show placement/5.
%For debugging purposes
%#show follows/2.