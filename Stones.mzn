include "globals.mzn";

%Grid size
par int: n;
%Number of stones
par int: t = 14;
%Is symmetry breaking disabled?
par bool: symm = true;
%Aviable stones
array [1..t,1..2] of 0..6: Stones =   [| 0, 1
                                       | 1, 1
                                       | 2, 1
                                       | 1, 4
                                       | 3, 0
                                       | 0, 0
                                       | 2, 4
                                       | 0, 1
                                       | 1, 1
                                       | 2, 1
                                       | 1, 4
                                       | 3, 0
                                       | 0, 0
                                       | 2, 4
                                       |];

%Array of placed values, in order. Second and third values are the coordinates x and y of the move
%All numbers are upshifted by 1, 0 is the special value for missing placements
array [1..4,1..n^2] of var 0..(max(max(n,t),6)): Placements;

%Coordinates are bound to grid size
constraint forall(i in 1..n^2)(Placements[2,i] <= n /\ Placements[3,i] <= n /\ Placements[2,i] > 0 /\ Placements[3,i] > 0);

%No two placements can be on the same spot in the grid

%array [1..n^2] of var int: Unfolded_positions;
%constraint forall (i in 1..n^2)(Unfolded_positions[i] = Placements[2,i]*(n+1) + Placements[3,i]);
%constraint all_different(Unfolded_positions);
constraint all_different((i in 1..(n^2)))(Placements[2,i]*(n+1) + Placements[3,i]);

%Even placements need to be equal to the following one
constraint forall(i in 1..((n^2-1) div 2))(Placements[1,2*i] = Placements[1,2*i+1] \/ Placements[1,2*i+1] = 0);
%First placement needs to be legal
constraint exists(i in 1..t)(Placements[1,1] = Stones[i,1]+1 \/ Placements[1,1] = Stones[i,2]+1);

%Odd placements require the following one to be constrained by the possible tiles. Tile values are upshifted by 1 to make the 0 a special value
constraint forall(i in 0..((n^2-2) div 2))(
                                            exists(j in 1..t)( (
                                                                (Placements[1,i*2+1] = Stones[j, 1]+1 /\ Placements[1,i*2+2] = Stones[j, 2]+1) \/
                                                                (Placements[1,i*2+1] = Stones[j, 2]+1 /\ Placements[1,i*2+2] = Stones[j, 1]+1)
                                                                 ) /\ 
                                                                (Placements[4,i*2+1] = j /\ Placements[4,i*2+2] = j)
                                                              ) \/
                                            (Placements[1, i*2+1] = 0 /\ Placements[1, i*2+2] = 0)
                                           );
                                           
%Cannot use same tile multiple times
constraint forall(i in 2..n^2, j in 1..(i-2))((Placements[1,i] != 0) -> (Placements[4,i] != Placements[4,j]));

%Following placements need to be adjacent
constraint forall(i in 1..(n^2-1))((abs(Placements[2,i] - Placements[2,i+1]) + abs(Placements[3,i] - Placements[3,i+1])) = 1
                                    \/ Placements[1,i] = 0);

%Cannot place two tiles with two adjacent cells back to back. Aka even placements cannot be adjacet to the placements 3 moves back
%constraint forall(i in 2..((n^2) div 2))((abs(Placements[2,2*i] - Placements[2,2*i-3]) + abs(Placements[3,2*i] - Placements[3,2*i-3])) > 1);

%%%%%%%%%%%%%%%%%%%
%SYMMETRY BREAKING%
%%%%%%%%%%%%%%%%%%%

%First placement is in a fixed quarter of the grid (avoids vertical and horizontal symmetries)
constraint Placements[2,1] < n/2 + 1 /\ Placements[3,1] < n/2 + 1 \/ not symm;
%Avoid reverse placement order symmetry
constraint Placements[4,1] <= Placements[4,n^2-non_placements] \/ not symm;
%If grid is too big for aviable tiles, work on a sub-grid and ignore cells outside of it
constraint forall(i in 1..n^2)((i > t*2 \/ Placements[2,i] > t*2 \/ Placements[3,i] > t*2) -> (Placements[1,i] = 0)) \/ not symm;
%Do not bother with the values of non-placements
%constraint forall(i in 1..n^2)(Placements[1,i] = 0 -> (Placements[2,i] = Placements[3,i] /\ Placements[3,i] = Placements[4,i] /\ Placements[4,i] = 0));
%Identical stones cannot be swapped (seems to make performance considerably worse)
constraint forall(i in 1..n^2,j in 1..i-1)(((Stones[Placements[4,i],1] = Stones[Placements[4,j],1] /\ 
                                            Stones[Placements[4,i],2] = Stones[Placements[4,j],2]) \/
                                            (Stones[Placements[4,i],1] = Stones[Placements[4,j],2] /\ 
                                            Stones[Placements[4,i],2] = Stones[Placements[4,j],1])) ->
                                            (Placements[4,j] <= Placements[4,i])) \/ not symm \/ true;

%%%%%%%%%%%%%%%%%%
%COST CALCULATION%
%%%%%%%%%%%%%%%%%%

var 0..n^2: non_placements = count(Placements[1,1..n^2], 0);

%Explicit cap to non_placements to stop search early when optimum has been reached
constraint non_placements >= n^2 - (t * 2);
constraint (n mod 2 = 1 -> non_placements >= 1);

solve :: int_search(Placements, dom_w_deg, indomain_min) minimize non_placements