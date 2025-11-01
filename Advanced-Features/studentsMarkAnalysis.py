import numpy as np

def analyze_marks(marks):
    avg = round(np.mean(marks), 2)
    min_mark = np.min(marks)
    max_mark = np.max(marks)
    return avg, min_mark, max_mark

def classify_grades(marks):
    grades=[]
    for mark in marks:
        if mark >= 90:
            grades.append("A")
        elif mark>=80:
            grades.append("B")
        elif mark>=70:
            grades.append("C")
        else:
            grades.append("D")
    return grades
    
if __name__ == "__main__":
    print("Student Marks Analysis")
    print("-----------------------")
    marks = [85, 92, 78, 65, 88, 72]
    avg, min_mark, max_mark = analyze_marks(marks)
    grades = classify_grades(marks)

    print("Average Mark:", avg)
    print("Minimum Mark:", min_mark)
    print("Maximum Mark:", max_mark)
    print("Grades:", grades)
