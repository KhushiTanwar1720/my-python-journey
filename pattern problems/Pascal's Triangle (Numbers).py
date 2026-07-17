for i in range(5):
    num = 1
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(f"{num:3}",end=" ")
        num = num*(i-j) // (j+1)
    print()