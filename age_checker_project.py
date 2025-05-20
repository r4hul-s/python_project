#birthday calculator program using python...
from datetime import datetime, date

birth_date = input("Enter your Birth Date in dd-mm-yyyy format: ")
b_date = datetime.strptime(birth_date, "%d-%m-%Y").date()# strptime = this will convert string into date 
today = date.today() #this  will get todays date 
print("Today's Date is...: ", today)
age = today.year - b_date.year
if (today.month, today.day) < (b_date.month, b_date.day): #(5,14)< (04,12)
    age -= 1 # age=age-1 
print ("Your age is..", age)

next_birthday = b_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_left = (next_birthday - today).days
print("Days until your next birthday:", days_left)

#add changes to make a pull request 
#changes committed
