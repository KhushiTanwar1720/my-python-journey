for i in range(5):
    for j in range(5-(i+1)):
        print(" ",end=" ")
    for j in range(i):
        print(chr(65+j),end=" ")
    for j in range(i,-1,-1):
        print(chr(65+j),end=" ")
    print()