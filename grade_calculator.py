
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input("Enter marks for " + subject + ": "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Please enter a number. Try again.")



def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"



def has_passed(marks):
    for mark in marks:
        if mark < 35:
            return False
    return True


def main():
    name = input("Enter student name: ")
    subjects = ["Mathematics", "Programming", "English", "Physics", "Database"]
    marks = []

    for subject in subjects:
        marks.append(get_valid_mark(subject))

    total = sum(marks)
    percentage = total / len(subjects)
    grade = get_grade(percentage)

    print("\n" + "=" * 32)
    print("       STUDENT GRADE REPORT")
    print("=" * 32)
    print("Name: " + name)
    print("\nSubject Marks:")
    for index in range(len(subjects)):
        print(subjects[index] + ": " + str(marks[index]))

    print("\nTotal Marks: " + str(total) + " / 500")
    print("Average / Percentage: " + str(round(percentage, 2)) + "%")
    print("Grade: " + grade)

    if has_passed(marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")
    print("=" * 32)


main()
