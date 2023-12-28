# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()


#number of t,r,u,e / l,o,v,e in name1

a_t = name1_lower.count('t')
a_r = name1_lower.count('r')
a_u = name1_lower.count('u')
a_e = name1_lower.count('e')

a_l = name1_lower.count('l')
a_o = name1_lower.count('o')
a_v = name1_lower.count('v')
a_e = name1_lower.count('e')

#number of t,r,u,e / l,o,v,e in name2

b_t= name2_lower.count('t')
b_r= name2_lower.count('r')
b_u= name2_lower.count('u')
b_e= name2_lower.count('e')

b_l= name2_lower.count('l')
b_o= name2_lower.count('o')
b_v= name2_lower.count('v')
b_e= name2_lower.count('e')



#number of t,r,u,e in name1 and name1

t_total = a_t + b_t
r_total = a_r + b_r
u_total = a_u + b_u
e_total = a_e + b_e


#number of l,o,v,e in name1 and name1


l_total = a_l + b_l
o_total = a_o + b_o
v_total = a_v + b_v
e_total = a_e + b_e



true_total = str(t_total + r_total + u_total + e_total)
love_total = str(l_total + o_total + v_total + e_total)




love_score = true_total + love_total



if int(love_score) < 10 or int(love_score) > 90:
    print(f'Your score is {love_score}, you go to together like coke and mentos.')
    
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f'Your score is {love_score}, you are alright together.')

else:
    print(f'Your score is {love_score}.')





