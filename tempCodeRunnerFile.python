contact = [
    ["Khushi",9670345678],
    ["Rohan",8902345679],
    ["Tushar",8767890567],
    ["Vaijanti",8456790238]
]

while True:
 Name = input("enter name:")
 Number = input("enter number:")
 contact.append([Name , Number])

 for x in contact:
    print(x)

 search_name = input("enter name to search:")
 found = False
 for person in contact:
    if person[0].lower() == search_name.lower():   
     print("contact found:" , person)
     found = True
     break

 if not found:
   print("contact not found")

 delete_name = input("enter name to delete :")
 found = False
 for person in contact:
   if person[0].lower() == delete_name.lower():
      contact.remove(person)
      print("contact deleted")
      found = True
      break
 if not found:
   print("contact not found")

 choice = input("Do you want to use this? (yes/no)").lower()
 if choice != "yes":
  print("Thank you!")
  break

      