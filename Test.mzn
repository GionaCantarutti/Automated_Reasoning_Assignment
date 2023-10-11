%include "globals.mzn";

par int: n;

array [1..n] of var 1..n^2: t;

var int: sum = sum(i in 1..n)(t[i]);

%constraint all_different(t);

solve :: int_search(t, dom_w_deg, indomain_min) minimize sum;