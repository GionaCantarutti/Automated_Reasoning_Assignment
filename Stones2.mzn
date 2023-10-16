include "globals.mzn";

%Grid size
par int: n;
%Number of stones
par int: t;
%Is symmetry breaking disabled?
par bool: symm = true;
%Aviable stones
array [1..t,1..2] of 0..6: Stones;
%                                      [| 0, 1
%                                       | 1, 1
%                                       | 2, 1
%                                       | 1, 4
%                                       | 3, 0
%                                       | 0, 0
%                                       | 2, 4
%                                       | 0, 1
%                                       | 1, 1
%                                       | 2, 1
%                                       | 1, 4
%                                       | 3, 0
%                                       | 0, 0
%                                       | 2, 4
%                                       |];

%Choice of stones to place in each square, in order. 0 is a non-placement
array [1..n^2] of var 0..t: Placements;
%Side of stone on that placements, in order
array [1..n^2] of var 1..2: Sides;
%Coordinates of each placement, in order
array [1..2,1..n^2] of var 1..n: Coordinates;


%Coordinates need to be all different
constraint all_different(i in 1..(n^2) - non_placements)(Coordinates[1,i]*(n+1) + Coordinates[2,i]);
%Even placements need to be the same as the previous one (single tile occupies two placements) but opposite side of tile
constraint forall(i in (1..n^2 div 2))(Placements[2*i] = Placements[2*i - 1] /\ Sides[2*i] != Sides[2*i - 1]);
%Odd placements need to have the same tile value as the previous one
constraint forall(i in (1..(n^2-1) div 2))(Stones[Placements[2*i + 1], Sides[2*i + 1]] = Stones[Placements[2*i], Sides[2*i]]
                                           \/ Placements[2*i+1] = 0);
%Coordinates of time-adjacent placements must also be space-adjacent
constraint forall(i in 2..n^2 - non_placements)(abs(Coordinates[1, i] - Coordinates[1, i-1]) + abs(Coordinates[2,i] - Coordinates[2, i-1]) = 1);
%The same tile cannot be used twice
constraint all_different(i in 1..(n^2 - non_placements) div 2)(Placements[2*i]);

%%%%%%%%%%%%%%%%%%%
%SYMMETRY BREAKING%
%%%%%%%%%%%%%%%%%%%

%If the board has an odd side length, the last placement is always empty
constraint (n mod 2 = 1) -> (Placements[n^2] = 0);
%Force placing first tile in one quarter of the board to break vertical and horizontal symmetries
constraint Coordinates[1,1] < n/2 + 1 /\ Coordinates[2,1] < n/2 + 1;
%Break symmetry that would allow to place the same tiles but in reverse order
constraint (n > 1) -> (Placements[1] < Placements[n^2 - non_placements]);
%Prevent swapping of equivalent tiles (seems to significantly worsen performance)
constraint forall(i in 1..n^2 - non_placements, j in 1..i-2)(((
                                               (Stones[Placements[i], 1] = Stones[Placements[j], 1]
                                               /\ Stones[Placements[i], 2] = Stones[Placements[j], 2]) \/
                                               (Stones[Placements[i], 1] = Stones[Placements[j], 2]
                                               /\ Stones[Placements[i], 2] = Stones[Placements[j], 1]))
                                               -> Placements[i] > Placements[j]))
                                               \/ true; %Disabled
%Stop if all tiles have been used
constraint non_placements >= n^2 - t*2;
%If grid is too large, ignore a portion of it
%constraint forall(i in (1..n^2), j in 1..2)(Placements[i] != 0 -> Coordinates[j,i] <= sqrt(t)+1);
%constraint forall(i in (1..n^2), j in 1..2)(Coordinates[j,i] < sqrt(t)+1);

var int: non_placements = count(Placements, 0);

solve :: int_search(Placements, dom_w_deg, indomain_min) minimize non_placements;

%output [if (i mod n+1 > 0)
%        then "\(Stones[Placements[i],Sides[i]])"
%        else "\n"
%        endif
%        |i in 1..(n+1)^2];