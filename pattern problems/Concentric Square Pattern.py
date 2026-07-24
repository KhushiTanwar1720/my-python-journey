n = 5
for i in range(9):
    for j in range(9):
        Top    = i
        Left   = j
        Bottom = (2*n - 2) - i
        Right  = (2*n - 2) - j
        layer = min(Top, Left, Bottom, Right)
        value = n - layer
        print(value,end=" ")
    print()