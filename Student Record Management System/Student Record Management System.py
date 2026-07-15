print("---Student Record Management System---")

student_record = [
{"Student_ID":"101","Name":"Khushi","Age":"19","Course":"BTech","Marks":"89","Grade":"A"},
{"Student_ID":"102","Name":"Vanshu","Age":"20","Course":"BTech","Marks":"76","Grade":"B"},
{"Student_ID":"103","Name":"Sarthak","Age":"21","Course":"BTech","Marks":"65","Grade":"C"}
]

while True:
    print(" 1. Add Student Record")
    print(" 2. View All Student Records")
    print(" 3. Search Student Record")
    print(" 4. Update Student Record")
    print(" 5. Delete Student Record")
    print(" 6.Display Topper")
    print(" 7. Display Passed/Failed Students")
    print(" 8. Count Total Students")
    print(" 9. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\n---Add Student Record---")
        Student_ID = input("Enter Student_ID: ")
        Name = input("Enter the name: ")
        Age = input("Enter the age: ")
        Course = input("Enter the course: ")
        Marks = input("Enter the marks: ")
        Grade = input("Enter the grade: ")
        
        duplicate = False
        for student in student_record: 
            if student["Student_ID"] == Student_ID:
                duplicate = True
                print("Student_ID already exist: ")
                break
        if duplicate == False:       
            new_student = {"Student_ID":Student_ID , "Name":Name, "Age":Age, "Course":Course, "Marks":Marks, "Grade":Grade}
            student_record.append(new_student)
            print("Student_ID added successfully: ")
                
    elif choice == "2":
        print("\n---student list---")
        for student in student_record:
            print( "Student_ID" ,":" , student["Student_ID"] )
            print("Name" , ":" ,student["Name"] )
            print( "Age" ,":" , student["Age"] )
            print( "Course" ,":" , student["Course"] )
            print( "Marks" ,":" , student["Marks"] )
            print( "Grade" ,":" , student["Grade"] )
                
    elif choice == "3":
        print("\n---Search Student Record---")
        search_Student_ID = input("Enter the Student_ID: ")
        found = False
        for student in student_record:
            if student["Student_ID"] == search_Student_ID:
                found = True 
                print("Student_ID" ,":",student["Student_ID"])
                print("Name" ,":",student["Name"])
                print("Age" ,":",student["Age"])
                print("Course" ,":",student["Course"])
                print("Marks" ,":",student["Marks"])
                print("Grade" ,":",student["Grade"])
                print()
                break
        if found == False:
            print("Student Record not found. ")
            
    elif choice == "4":
        print("\n---Update Student Record---")
        update_Student_ID = input("Enter the Student_ID: ")
        found = False
        for student in student_record:
            if student["Student_ID"] == update_Student_ID:
                found = True 
                new_name = input("Enter new Name: ")
                student["Name"] = new_name
                new_age =input("Enter new Age: ")
                student["Age"] = new_age
                new_course =input("Enter new Course: ")
                student["Course"] = new_course
                new_marks = input("Enter new Marks: ")
                student["Marks"] = new_marks
                new_grade =input("Enter new Grade: ")
                student["Grade"] = new_grade
                print("Student record updated successfully.")
                print()
                break
        if found == False:
            print("Student Record does not exist. ")
            
    elif choice == "5":
        print("\n---Delete Student Record---")
        delete_student_id = input("Enter Student_ID: ")
        found = False
        for student in student_record:
            if student["Student_ID"] == delete_student_id:
                found = True
                student_record.remove(student)
                print("Student Record deleted successfully. ")
                print()
                break
        if found == False:
            print("Student Record not found. ")
    elif choice == "6":
        print("\n---Display Topper---")
        topper = student_record[0]
        for student in student_record:
            if int(student["Marks"]) > int(topper["Marks"]):
                topper = student
        print("Student_ID" ,":",topper["Student_ID"])
        print("Name" ,":",topper["Name"])
        print("Age" ,":",topper["Age"])
        print("Course" ,":",topper["Course"])
        print("Marks" ,":",topper["Marks"])
        print("Grade" ,":",topper["Grade"])
        print()
    elif choice == "7":
        print("\n---Passed Students---")
        for student in student_record:
            if int(student["Marks"]) >= 40:
                print("Student_ID" ,":",student["Student_ID"])
                print("Name" ,":",student["Name"])
                print("Age" ,":",student["Age"])
                print("Course" ,":",student["Course"])
                print("Marks" ,":",student["Marks"])
                print("Grade" ,":",student["Grade"])
                print()
        print("\n---Failed Students---")
        for student in student_record:
            if int(student["Marks"]) < 40:
                print("Student_ID" ,":",student["Student_ID"])
                print("Name" ,":",student["Name"])
                print("Age" ,":",student["Age"])
                print("Course" ,":",student["Course"])
                print("Marks" ,":",student["Marks"])
                print("Grade" ,":",student["Grade"])
                print()
    elif choice == "8":
        print("\n---Count Total Students---")
        total_students = len(student_record)
        print("Total Students:" , total_students )
        
    elif choice == "9":
        print("Exiting Student Record... ")
        break
    else:
        print("Invalid choice. ")
