user = int(input("Enter the number:"))
if 0 <= user <=12:
    print("child")
elif 12 <= user <= 19:
    print("Teenager") 
elif 20 <= user <=59:
    print("Adult")
elif 60 <= user <=1000:
    print("Senior")
else:
    print("invalid")