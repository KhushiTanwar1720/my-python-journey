for i in range(5):
    for j in range(5-(i+1)):
            print(" ",end=" ")
    if i == 0:
        print(chr(65),end=" ")
    else:
            print(chr(65+i),end="")
            for j in range((4*i)-1):
                print(" ",end="")
            print(chr(65+i),end="")
    print()
for i in range(4):
    for j in range(i+1):
        print(" ",end=" ")
    if i == 3:
        print("A",end=" ")
    else:
            print(chr(65+(3-i)),end="")
            for j in range(11-(i*4)):
                print(" ",end="")
            print(chr(65+(3-i)),end="")
    print()