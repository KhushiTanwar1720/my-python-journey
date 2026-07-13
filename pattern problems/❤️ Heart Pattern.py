i = 0
#upper half
for i in range(3):
    #left spaces
    for j in range(2-i):
        print(" ",end=" ")
    #Left pyramid
    for j in range((i*2)+1):
        print("*",end=" ")
    #Middle spaces
    for j in range(4-(i*2)):
        print(" ",end=" ")
    #Right pyramid
    for j in range((i*2)+1):
        print("*",end=" ")
    print()
#lower half
for i in range(5):
    #lower spaces
    for j in range(i*2):
        print(" ",end="")
    #lower stars
    for j in range(9-(i*2)):
        print("*",end=" ")
    print()