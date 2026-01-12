# Make a number analyzer that works : take input a number from user, check and print positive/negative/zero and even/odd, ask user for check another number or not.(not use function)
while True:
    num = int(input("Enter a number : "))

    if num>0:
        print("Positve")
    elif num<0 :
        print("Negative")
    else:
        print("Zero")

    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

    # ask user for repeat
    user_de = input("Do you want check another number (yes/no): ").lower()
    if user_de == "no":
        print("Program ended...")
        break
    elif user_de =="yes":
        continue
    else:
        print("Invalid input! Please type 'yes' or 'no' ")
        break