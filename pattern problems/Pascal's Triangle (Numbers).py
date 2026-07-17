num = 1
for i in range(5):
    for j in range(5-(num+1)):
        print(" ",end=" ")
    for j in range(num+1):
        print(num,end=" ")
        num *= 11
    print()