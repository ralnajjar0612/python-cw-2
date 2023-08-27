My_name = input("My name is: ")
My_age = int(input('my age is: '))
print(f"My name is {My_name} and I am {My_age} years old.")

First_number= int(input("Your First numer is: "))
Second_number= int(input ("Your Second number is: "))
Operation= input("Your prefered Operation sign is: ")

if Operation == "+":
    print(First_number + Second_number)

elif Operation == "-":
    print(First_number - Second_number)

elif Operation == "*":
    print(First_number * Second_number)

elif Operation == "/":
    print(First_number / Second_number)

else:
    print("The operation is not valid.")

Bus_capacity = 40
people_inbus= int(input("People in the bus:"))
print(f"there are {people_inbus} people in the bus.")
people_waiting= int(input("People waiting outside of the bus:"))
print(f"there are {people_waiting} people waiting.")

empty_seats= (Bus_capacity - people_inbus)
if people_inbus < Bus_capacity:
    print(f"There are {empty_seats} empty seats.")

else:
    print("The bus is full.")
