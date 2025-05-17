days_unit = 24
unit = "hours"


def days_to_hours(num_days):
    if num_days > 0:
        return f"In {num_days} days there are {num_days*days_unit} {unit} " # whern we are taking input fromthe user we always use return statement rather than print statement 
    elif num_days == 0:
        return f"Number of Days can't be {num_days}"
    else:
        return "Invalid Input..."


usr_input = int(input("Enter the Number of Days you want to convert into hours\n"))
calc_value = days_to_hours(usr_input) #calling function by creating variable for user input 
print(calc_value)# for displaying the result

#comparison operators  ==(equals to), >(greater),<(less),!=(not equals),>=(greater equals),<=(less equals)
# ** -> exponentian operator use 2**3 = 8
# // floor division operator 
'''print(7 // 2)    # Output: 3
print(7.0 // 2)  # Output: 3.0
print(-7 // 2)   # Output: -4  (floors down to -4)'''
