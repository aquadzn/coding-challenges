function countSumOfTwoRepresentations3(n: integer; l: integer; r: integer): integer;
begin
  exit(max(n div 2 - max(l, n-r) + 1, 0))
end;