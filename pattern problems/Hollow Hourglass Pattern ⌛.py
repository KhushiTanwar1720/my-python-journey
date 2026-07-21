n = 5
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*n - 1 - 2*i):
        if i == 0 or j == 0 or j == (2*n-2-2*i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
for i in range (1,n):
    for j in range( n-i-1):
        print(" ",end =" ")
    for j in range(2*i+1):
        if  i == n-1 or j == 0 or j == i*2 :
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print()