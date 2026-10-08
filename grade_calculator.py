"""
Student Grade Calculator

Version: 1.1.2
"""

def calculate_average(marks):
    """Calculate the average of a list of marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_result(average):
    """Determine whether the student passed or failed."""
    if average > 50:
        return "PASS"
    else:
        return "FAIL"

def main():
    student_name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    average = calculate_average(marks)
    result = get_result(average)

    print("\nStudent:", student_name)
    print("Average:", round(average, 2))
    print("Result:", result)

if __name__ == "__main__":
    main()