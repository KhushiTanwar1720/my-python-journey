i = 0
for i in range(5):
    for j in range(i+1):
        if j == i or j == 0 :
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(8-(i*2)):
        print(" ",end="")
    for j in range(i+1):
        if j == i or j == 0:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(4):
    for j in range(4-i):
        if j == 3-i or j == 0:
            print("*",end="")
        else:
            print(" ",end="")
    for j in range((i*2)+2):
        print(" ",end="")
    for j in range(4-i):
        if  j == 3-i or j == 0:
            print("*",end="")
        else:
            print(" ",end="")
    print()