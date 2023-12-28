def name(f_name, l_name):
    
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    
    return f'{new_f_name} {new_l_name}'
    
    
    
one_name = input('enter your first name: ')
sec_name = input('enter your second name: ')   

print(name(one_name, sec_name))


