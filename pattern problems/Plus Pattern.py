i = 0
for i in range(5):
    for j in range(5):
        if j == 2 or i == 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()