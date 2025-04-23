def studentGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 70:
        return "B"
    elif grade >= 50:
        return "C"
    elif grade >= 35:
        return "D"
    else:
        return "Fail"


grade = int(input("Enter your grade: "))

result = studentGrade(grade)
print(f"Your grade is: {result}")
