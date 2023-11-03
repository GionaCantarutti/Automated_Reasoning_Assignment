%%%%% RULES %%%%%
%stone facts have format stone((N1, N2), ID) where N1 and N2 are the two numbers on the stone and ID is the stone's unique identifier (supposed to be incremental, starting at 1)
%board size constant is named n
%%%%% RULES %%%%%
%basic facts
size(n).
time(1..(n**2)).
coordinates(1..n,1..n).
%placement time = 0 means no placement
1 { placement(1..n, 1..n, 0..(n**2), A, ID) } 1 :- stone((A, _), ID).
1 { placement(1..n, 1..n, 0..(n**2), B, ID) } 1 :- stone((_, B), ID).
%each cell has up to one placement
3 { T = T1; A = A1; ID = ID1 } 3 :- coordinates(X, Y), placement(X, Y, T, A, ID), placement(X, Y, T1, A1, ID1), stone((A, _), ID), time(T).
%time-adjacent placements also need to be space-adjecent
1 {X1 = X + 1; X1 = X - 1; Y1 = Y + 1; Y1 = Y - 1} 1:- placement(X, Y, T, _, _), placement(X1, Y1, T + 1, _, _), coordinates(X, Y), coordinates(X1, Y1), time(T).

%%%% OPTIMIZATION %%%%
:~ placement(_, _, 0, _, _). [1@1]
#show placement/5.