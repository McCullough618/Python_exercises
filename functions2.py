Student = input("Please enter student name ")
homework = int(input("Please enter homework score "))
assessment = int(input("Please enter assessment score "))
final_exam = int(input("Please enter final exam score "))

def total_marks(homework, assessment, final_exam):
    answer = homework + assessment + final_exam
    return answer
ICT_marks = total_marks(homework, assessment, final_exam)/175*100
print(ICT_marks)

if ICT_marks>69:
    print("ICT Grade = A")
elif ICT_marks>59:
    print("ICT Grade = B")
elif ICT_marks>49:
    print("ICT Grade = C")
elif ICT_marks<50:
    print("ICT Grade = F")
