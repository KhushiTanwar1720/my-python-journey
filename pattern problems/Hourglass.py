i = 0
for i in range(5):
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(9-(i*2)):
        print("*",end=" ")
    print()
for i in range(4):
    for j in range(7-(i+2)):
        print(" ",end=" ")
    for j in range(3+(i*2)):
        print("*",end=" ")
    print()