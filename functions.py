def addCalc(number1, number2):
    answer = number1 + number2
    return answer
addedNuner = addCalc(5,5)
print(addedNuner + 20)

def total_marks(homework, assessment, final_exam):
    answer = homework + assessment + final_exam
    return answer
ICT_grade = total_marks(5+10+20)/175*100
print(ICT_grade)

Student = input("Please enter student name")
homework = input("Please enter homework score")
assessment = input("Please enter assessment score")
final_exam = input("Please enter final exam score")

def total_marks(homework, assessment, final_exam):
    answer = homework + assessment + final_exam
    return answer
ICT_grade = total_marks(homework, assessment, final_exam)/175*100
print(ICT_grade)
