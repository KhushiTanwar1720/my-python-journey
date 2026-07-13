i = 0
for i in range(5):
    for j in range(5):
        if j == 4-i or j == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()