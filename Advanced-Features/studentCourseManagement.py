
def Student_names():
    students = ["John", "Doe", "Jane", "Smith"]

    # Append new Student Olivia
    students.append("Olivia")

    return students


def student_course():
    student_courses = {
        "John":("Math","Science"),
        "Emma":("History", "English"),
        "Michael":("Physics", "Chemistry"),
        "Sophia":("Biology", "Art")
    }
    student_courses["Olivia"] = ("Biology", "History")
    return student_courses

def unique_subjects():
    subjects =["Math","Science","Biology","Math","English","Science"]

    subjects.append("Economics")
    unique_set = set(subjects)
    return unique_set

if __name__ == "__main__":
    student_names = Student_names()
    print("Student Names:", student_names)

    updated_student_courses = student_course()
    print("Student Courses:")
    for student, courses in updated_student_courses.items():
        print(f"{student}: {courses}")

    unique_subjects = unique_subjects()
    print("Unique Subjects:", unique_subjects)
    
