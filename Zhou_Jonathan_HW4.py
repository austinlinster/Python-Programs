#Jonathan Zhou
#October 3rd, 2022
#MIS 304 Grade Calculator

#Global Constants
EXAM1_WEIGHT = .2
EXAM2_WEIGHT = .2
EXAM3_WEIGHT = .2
HOMEWORK_ASSIGNMENTS_WEIGHT = .3
FINAL_PROJECT_WEIGHT =.1

#Take inputs for grades for assignments using assignment name as parameter
def get_grade(assignment_name):
    grade = float(input(f'What is your grade for {assignment_name}: '))

    while grade < 0 or grade > 100:
        print("Grade must be a number between 0 - 100")
        grade = float(input(f'What is your grade for {assignment_name}: '))
    return grade

#Calculate and return the numeric grade using the 5 assignments as parameters
def calc_average(exam_1, exam_2, exam_3, homework, final):
    global average
    average = (exam_1 * EXAM1_WEIGHT+ exam_2 * EXAM2_WEIGHT+ exam_3 * EXAM3_WEIGHT+ homework * HOMEWORK_ASSIGNMENTS_WEIGHT+ final * FINAL_PROJECT_WEIGHT) 
    print(f'Final Numeric Grade: {average:.2f}')
    
#Determine letter grade based on numeric parameter
def calc_letter(average):
    if average >= 89.5:
        letter_grade = "A"
    elif average >= 79.5:
        letter_grade = "B"
    elif average >= 69.5:
        letter_grade = "C"
    elif average >= 59.5:
        letter_grade = "D"
    else:
        letter_grade = "F"
    print(f'Final Letter Grade: {letter_grade}')


#Main Function Calls other functions inside to run their code
def main():
    exam1val = get_grade("Exam 1")
    exam2val = get_grade("Exam 2")
    exam3val = get_grade('Exam 3')
    homeworkval = get_grade("Homework")
    finalval = get_grade("Final Project")
    calc_average(exam1val, exam2val, exam3val, homeworkval, finalval)
    calc_letter(average)

#Executing Main Function
# main()