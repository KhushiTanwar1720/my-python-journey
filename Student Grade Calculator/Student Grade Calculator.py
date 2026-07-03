marks1 = float(input("Enter the marks1"))
marks2 = float(input("Enter the marks2"))
marks3 = float(input("Enter the marks3"))
Total = marks1 + marks2 + marks3
if (marks1 < 0 or marks1>100 or marks2 < 0 or marks2>100 or marks3 < 0 or marks3>100):
    print("Invalid input")
else:
    print("Total Marks:",Total)
    maximum_marks = 300
    Percentage = ( Total / maximum_marks )*100
    print(f"Percentage:{Percentage:.2f}%")
    if Percentage >= 90:
       print("Grade A")
    elif Percentage >=80:
       print("Grade B")
    elif Percentage >=70:
       print("Grade C")
    elif Percentage >=60:
       print("Grade D")
    else:
       print("Grade E") 