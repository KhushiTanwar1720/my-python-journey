i = 0
for i in range(5):
    for j in range(5-(i+1)):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end = " ")
    print()
for i in range(4):
    for v in range(i+1):
        print(" ",end=" ")
    for a in range(7-(i*2)):
        print("*",end = " ")
    print()