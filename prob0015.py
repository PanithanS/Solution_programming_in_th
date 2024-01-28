A,B,C = map(int, input().split())

moves = 0

while B - A > 1 or C - B > 1:
    span_AB = B - A
    span_BC = C - B
    if span_AB > span_BC:
        C = B
        B = A + 1
        moves += 1
    else:
        A = B
        B = C - 1
        moves += 1

print(moves)