i = 0
for i in range(5):
    for j in range(5-(i+1)):
        print(" ",end=" ")
    for k in range(i*2+1):
        if i == 0 or k == i*2 or k == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for v in range(4):
    for a in range(v+1):
        print(" ",end=" ")
    for n in range(7-(v*2)):
        if n == 0 or n == 6-(v*2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()