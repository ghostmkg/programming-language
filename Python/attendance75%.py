# Taking input for attendance percentage and medical issue
attendance = float(input("Enter the student's attendance percentage: "))
medical_issue = input("Does the student have a medical issue? (Y/N): ")

# Checking eligibility
if attendance < 75 and medical_issue.lower() == 'y':
    print("The student is allowed for examinations due to medical reasons.")
elif attendance <= 75:
    print("The student is allowed for examinations.")
else:
    print("The student is not allowed for examinations.")