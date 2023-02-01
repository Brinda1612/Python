print("   ENETR YOUR CHOICE  ")
print(" 1 for addition : ")
print(" 2 for subtraction : ")
print(" 3 for multiplication : ")
print(" 4 for division : ")

choice = int(input("enter your choice : "))

if (choice == 1):
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    print("addition of the given number is : " + str(a+b))

elif (choice == 2):
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    print("subtraction of the given number is : " + str(a-b))
    
elif (choice == 3):
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    print("multiplication of the given number is : " + str(a*b))
    
elif (choice == 2):
    a = int(input("enter number : "))
    b = int(input("enter number : "))
    print("division of the given number is : " + str(a/b))

else:
    print("please, enter valid choice :")
