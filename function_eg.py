def sum(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    if n2 == 0:
        return "invalid input..."
    return n1/n2

def mul(n1,n2):
    return n1*n2

while True:

    print("Enter your choices 1,2,3,4,5")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Division")
    print("4 for Multiplication")

    print("5 to Exit")


    choice = input("Enter choice 1/2/3/4/5...")
    if not choice.isdigit() or choice not in ("1","2","3","4","5"):
        print("Invalid choice! Please enter correct choice")
    

    if choice == "5":
        print("Exiting calculator")
        break
    if choice in("1","2","3","4"):
        try:

            num1 = int(input("Enter Num1\n"))
            num2 = int(input("Enter Num2\n"))

        except ValueError:
            print("Invalid Input, Try again...")
            continue

        if choice == '1':
            print(f"The result is: {sum(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {sub(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {div(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {mul(num1, num2)}")
        else:
            print("Invalid input")

