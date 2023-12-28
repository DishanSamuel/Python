#checking for hightest score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest = 0
for highest_no in student_scores:
    if highest_no > highest:
        highest = highest_no


print(f"The highest score in the class is: {highest}")


#note hear we can use the max or min function and this program will be easy
#test score
#78 65 89 86 55 91 64 89