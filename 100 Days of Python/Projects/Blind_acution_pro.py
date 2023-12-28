import os
#HINT: You can call clear() to clear the output in the console.
# lec no 95 . refer this lec for different solution



print('Welcome to secret auction program')

members = {'name': [], 'bid_amount': []}

loop_status = True

while loop_status == True:
    name = input('what is you name?? : \n')
    bid_amount = input("what's your bid amount ?? : \n$") 
    loop = input("are there any bidders 'yes' or 'no' :\n")

    members['name'].append(name)
    members['bid_amount'].append(bid_amount)

    if loop == 'yes':
        loop_status = True
        # Clearing the Screen
        os.system('cls')
    else:
        loop_status = False

        max_bid = max(members['bid_amount'])

        position = members['bid_amount'].index(max_bid)

        bid_winner = members['name'][position]

        # Clearing the Screen
        os.system('cls')

        print(f'The winner is {bid_winner} with a bid of ${max_bid} ')
        
        
        
        
        
        
