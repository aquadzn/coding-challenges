function divideAsLongAsPossible(n: integer; d: integer): integer;
begin
while n mod d = 0 do
  begin
    n := n div d;
  end;
Exit(n);
end;
