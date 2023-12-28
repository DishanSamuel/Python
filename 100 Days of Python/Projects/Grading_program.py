# (lec no 92 ) 100 days of programming

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

for students in student_scores:
        if student_scores[students] >= 91 and student_scores[students] <= 100 :
            student_grades[students] = 'Outstanding'
            
        if student_scores[students] >= 81 and student_scores[students] <= 90 :
            student_grades[students] = 'Exceeds Expectations'
            
        if student_scores[students] >= 71 and student_scores[students] <= 80 :
            student_grades[students] = 'Acceptable'
            
        if student_scores[students] <= 70:
            student_grades[students] = 'Fail'
        
        
        
#to shorten the code we can add a separate variable (scores = student_scores[students])

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)