include "globals.mzn";

%Grid size
par int: n;
%Is symmetry breaking disabled?
par bool: symm = true;
%Aviable stones
%array [1..7,1..7] of int: Stones = [| 2, 2, 3, 5, 0, 0, 0
%                                    | 2, 2, 1, 2, 0, 0, 0
%                                    | 3, 1, 2, 0, 0, 0, 0
%                                    | 5, 2, 0, 2, 0, 0, 0
%                                    | 0, 0, 0, 0, 0, 0, 0
%                                    | 0, 0, 0, 0, 0, 0, 0
%                                    | 0, 0, 0, 0, 0, 0, 0
%                                    |]; %Values on diagonal should be even, representing twice the amount of desired stones
                                        %Matrix should be symmetirc wrt the diagonal

array [1..7,1..7] of int: Stones;

%Choice of stones to place in each square, in order
array [1..2, 1..n^2] of var 0..7: Placements;
%Coordinates of each placement, in order
array [1..2, 1..n^2] of var 1..n: Coordinates;

%A non-placement needs to be such on both sides
constraint forall(i in 1..n^2)(Placements[1, i] = 0 <-> Placements[2, i] = 0);
%Coordinates need to be all different
constraint all_different(i in 1..max(1, (n^2) - non_placements))(Coordinates[1,i]*(n+1) + Coordinates[2,i]);
%Even placements need to be from the same tile as the previous one , but opposite side
constraint forall(i in (1..n^2 div 2))(Placements[1, 2*i] = Placements[2, 2*i - 1] /\ Placements[2, 2*i] = Placements[1, 2*i - 1]);
%Odd placements need to have the same tile value as the previous one
constraint forall(i in (1..(n^2-1) div 2))(Placements[1, 2*i + 1] = Placements[1, 2*i]
                                           \/ Placements[1, 2*i+1] = 0 \/ Placements[2, 2*i+1] = 0);
%Coordinates of time-adjacent placements must also be space-adjacent
constraint forall(i in 2..max(2,n^2 - non_placements))(abs(Coordinates[1, i] - Coordinates[1, i-1]) + abs(Coordinates[2,i] - Coordinates[2, i-1]) = 1);
%Tiles can only be used an amount of times equal to how many of that tile you have
constraint forall(i in 1..7, j in 1..7)(
                                        sum(k in 1..n^2)(if (Placements[1,k] = i /\ Placements[2,k] = j)
                                                         then 1 else 0 endif)
                                        <= Stones[i,j]);

%%%%%%%%%%%%%%%%%%%
%SYMMETRY BREAKING%
%%%%%%%%%%%%%%%%%%%

%If the board has an odd side length, the last placement is always empty
constraint (n mod 2 = 1) -> (Placements[1, n^2] = 0);
%There can be no "gaps" in the placement sequence where no tiles where placed. Negligible impact on performance
%constraint forall(i in 2..n^2)(Placements[1, i] != 0 -> Placements[1, i-1] != 0);
%There can never be a placement following a non-placement (implied by previous heuristic)
constraint forall(i in 1..n^2-1)(Placements[1, i] = 0 -> Placements[1, i+1] = 0);
%Force placing first tile in one quarter of the board to break vertical and horizontal symmetries
constraint Coordinates[1,1] < n/2 + 1 /\ Coordinates[2,1] < n/2 + 1;
%Break symmetry that would allow to place the same tiles but in reverse order
constraint (n > 1) -> (Placements[1, 1] <= Placements[1, n^2 - non_placements]);
%Stop if all tiles have been used or entire grid has been filled
constraint non_placements >= max(n^2 - sum(i in 1..7, j in 1..7)(Stones[i,j]), 0);
%Coordinates of non-placements are irrelevant. This has MASSIVE impact on performance
constraint forall(i in 1..n^2)(Placements[1, i] = 0 -> (Coordinates[1,i] = 1 /\ Coordinates[2,i] = 1));
%If grid is too large, ignore a portion of it
%constraint forall(i in (1..n^2), j in 1..2)(Placements[i] != 0 -> Coordinates[j,i] <= sqrt(t)+1);
%constraint forall(i in (1..n^2), j in 1..2)(Coordinates[j,i] < sqrt(t)+1);

var int: non_placements = count(Placements[1, 1..n^2], 0);

solve :: int_search(Placements, dom_w_deg, indomain_min) minimize non_placements;

%output [if (i mod n+1 > 0)
%        then "\(Stones[Placements[i],Sides[i]])"
%        else "\n"
%        endif
%        |i in 1..(n+1)^2];