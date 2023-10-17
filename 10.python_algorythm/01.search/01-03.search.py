A,B,C,D,E,F = map(int, input().split())

for x in range(-999, 999 + 1):
    for y in range(-10_000, 10_000 + 1):
        if A * x + B * y == C:
            if D * x + E * y == F:
                print("{} {}".format(x, y))
                break