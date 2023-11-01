%instance

#const n = 5.

size(n).
%the two faces of a stone and a unqiue ID to allow duplicates
stone ((0,1),1).
stone ((1,0),2).
stone ((1,1),3).
stone ((2,0),4).
stone ((2,2),5).
stone ((6,2),6).
stone ((2,3),7).
stone ((3,5),8).
stone ((5,2),9).
stone ((5,0),10).
stone ((0,0),11).
stone ((5,2),12).
stone ((5,2),13).
stone ((0,2),14).
stone ((6,1),15).

%%%%% RULES %%%%%
%time
time(1..(n**2)).
%placement time = 0 means no placement
1 { placement(1..n, 1..n, 0..(n**2), A, ID) } 1 :- stone((A, _), ID).
1 { placement(1..n, 1..n, 0..(n**2), B, ID) } 1 :- stone((_, B), ID).
%each tile has up to one placement
3 { T = T1; A = A1; ID = ID1 } 3 :- X=1..n, Y=1..n, placement(X, Y, T, A, ID), placement(X, Y, T1, A1, ID1), stone((A, _), ID), time(T).

%%%% OPTIMIZATION %%%%
:~ placement(_, _, 0, _, _). [1@1]
#show placement/5.