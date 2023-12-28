#for avg height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0 
for height in student_heights:
    total_height += height

total_students = 0
for no_students in student_heights:
    total_students += 1

    
avg_height = round(total_height / total_students)

print(avg_height)



#note here we can use the sum and len functions and the code will be much easer
#this programs is to train the basics of for loops condition because in other programming languages there are no simple functions like sum and len
#test height
#156 178 165 171 187