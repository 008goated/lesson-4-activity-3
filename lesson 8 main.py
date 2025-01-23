medical_cause=input("did you have a mediacal cause Y or N")
attendance=int(input("Enter the attendence of student:"))
if medical_cause=="Y":
    print("you are allowed")
else:
    if attendance >=75:
        print("Allowed")
    else:
        print("not allowed")
         
