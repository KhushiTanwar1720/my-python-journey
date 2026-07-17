i = 0
for i in range(3):
    for j in range(9):
        if j == i or j == 8-i or j == 4-i or j == 4+i or j == 4 and i == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()